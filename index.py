import os
import asyncio
import logging
import mimetypes
import hashlib
from datetime import datetime
from telethon import TelegramClient, events
from PIL import Image, ExifTags, ImageFile
import piexif
import exifread
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

# Enable loading progressive/truncated JPEGs
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Logger setup
type_fmt = '%(asctime)s %(levelname)-8s: %(message)s'
logging.basicConfig(level=logging.INFO, format=type_fmt, datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# API Configs
API_ID = 23350184
API_HASH = '41f0c2a157268e158f91ab7d59f4fc19'
BOT_TOKEN = '7619515923:AAGlzmlklTqP3OXH-tgbdR3KHVEnwP0BZqc'
VERSION = "1.5.5"

# Initialize bot
bot = TelegramClient('info_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Start message
START_MESSAGE = (
    "🚀 **Capi Info Bot** v{} - Hoşgeldiniz! 📸\n"
    "----------------------------------------\n"
    "Bu bot ile medya dosyalarınızın **EXIF**, **dosya sistemi metadata**,\n"
    "**detaylı teknik metadata** ve **hash bilgilerini** kolayca alabilirsiniz.\n\n"
    "✨ **Komutlar:**\n"
    "   • `/start` - Başlatma mesajını gösterir.\n"
    "   • `/help`  - Yardım metnini tekrar gönderir.\n\n"
    "📖 **Nasıl Kullanılır?**\n"
    "   1️⃣ Fotoğraf, video veya belge gönderin.\n"
    "   2️⃣ Bot, size gerekli metadata bilgilerini iletecektir.\n"
    "----------------------------------------"
).format(VERSION)
HELP_MESSAGE = START_MESSAGE

# EXIF extractors
def extract_exif_pil(path):
    data = {}
    try:
        with Image.open(path) as img:
            img.load()
            raw = img.getexif() or {}
            for tag_id, val in raw.items():
                name = ExifTags.TAGS.get(tag_id, tag_id)
                data[name] = val
    except Exception as e:
        logger.warning(f"PIL EXIF hatası: {e}")
    return data

async def extract_exif_piexif(path):
    data = {}
    try:
        ex = piexif.load(path)
        if not isinstance(ex, dict):
            return data
        for ifd_dict in ex.values():
            if isinstance(ifd_dict, dict):
                for tag_id, val in ifd_dict.items():
                    name = piexif.TAGS.get('Exif', {}).get(tag_id, {}).get("name")
                    if name:
                        data[name] = val
    except Exception as e:
        logger.warning(f"piexif EXIF hatası: {e}")
    return data

async def extract_exif_exifread(path):
    data = {}
    try:
        with open(path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        for tag, val in tags.items():
            data[tag] = str(val)
    except Exception as e:
        logger.warning(f"exifread hatası: {e}")
    return data

async def extract_exif(path):
    exif = {}
    # JPEG, PNG - EXIFREAD
    exif.update(await extract_exif_exifread(path))
    # JPEG-only PIEEXIF
    exif.update(await extract_exif_piexif(path))
    # Fallback PIL
    exif.update(extract_exif_pil(path))
    # Normalize common tags
    norm = {}
    for k, v in exif.items():
        key = k.split()[-1]  # take last part: 'Make', 'Model', etc
        norm[key] = v
    exif = norm
    # GPS conversion
    try:
        if 'GPSLatitude' in exif and 'GPSLongitude' in exif:
            lat_vals = exif['GPSLatitude']
            lon_vals = exif['GPSLongitude']
            lat_ref = exif.get('GPSLatitudeRef', 'N')
            lon_ref = exif.get('GPSLongitudeRef', 'E')
            def dms_to_deg(dms):
                nums = [tuple(map(int, x.split('/'))) for x in dms.values()]
                return nums[0][0]/nums[0][1] + nums[1][0]/nums[1][1]/60 + nums[2][0]/nums[2][1]/3600
            lat = dms_to_deg(lat_vals)
            lon = dms_to_deg(lon_vals)
            if lat_ref == 'S': lat = -lat
            if lon_ref == 'W': lon = -lon
            exif['Latitude'] = round(lat,6)
            exif['Longitude'] = round(lon,6)
            exif['GoogleMapsLink'] = f"https://maps.google.com/?q={lat},{lon}"
    except Exception:
        pass
    return exif

# Hash hesaplama
def compute_hashes(path):
    sha256, md5 = hashlib.sha256(), hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
            md5.update(chunk)
    return sha256.hexdigest(), md5.hexdigest()

# Hachoir metadata
async def extract_hachoir(path):
    lines = []
    try:
        parser = createParser(path)
        metadata = extractMetadata(parser) if parser else None
        if metadata:
            for line in metadata.exportPlaintext():
                lines.append(line.strip())
        parser.stream.close()
    except Exception as e:
        logger.warning(f"Hachoir hatası: {e}")
    return lines

# Medya işle
async def process_media(event):
    path = await event.client.download_media(event.media)
    try:
        name = os.path.basename(path)
        size = os.path.getsize(path)
        mime, _ = mimetypes.guess_type(path)
        ctime = datetime.fromtimestamp(os.path.getctime(path)).isoformat(' ', 'seconds')
        mtime = datetime.fromtimestamp(os.path.getmtime(path)).isoformat(' ', 'seconds')
        sha256, md5 = compute_hashes(path)

        lines = [
            f"📂 **Dosya:** {name}",
            f"📐 **Boyut:** {size} byte",
            f"📁 **MIME:** {mime or 'Bilinmiyor'}",
            f"🕒 **Oluşturma:** {ctime}",
            f"🕒 **Değiştirme:** {mtime}",
            f"🔒 SHA256: `{sha256}`",
            f"🔒 MD5: `{md5}`",
        ]
        ext = os.path.splitext(path)[1].lower()
        if ext in ['.jpg','.jpeg','.tiff','.tif','.png']:
            exif = await extract_exif(path)
            if exif:
                lines.append("\n🛠️ **EXIF Bilgileri:**")
                for field in ['Make','Model','LensModel','Software','DateTimeOriginal']:
                    lines.append(f"- **{field}:** {exif.get(field,'Bilinmiyor')}")
                if 'Latitude' in exif:
                    lines.append(f"- **Konum:** {exif['Latitude']},{exif['Longitude']}")
                    lines.append(f"- [Haritada Göster]({exif['GoogleMapsLink']})")
                for field in ['ExposureTime','FNumber','ISOSpeedRatings','FocalLength']:
                    lines.append(f"- **{field}:** {exif.get(field,'Bilinmiyor')}")
            else:
                lines.append("ℹ️ EXIF bilgisi bulunamadı.")

        hachoir = await extract_hachoir(path)
        if hachoir:
            lines.append("\n🗃️ **Teknik Metadata:**")
            for l in hachoir:
                lines.append(f"- {l}")
        else:
            lines.append("⚠️ Derin analiz için `hachoir` kütüphanesi gerekli.")

        resp = '\n'.join(lines)
        if len(resp) > 4000:
            await event.reply("🔎 Metadata uzun, dosya olarak gönderiliyor.")
            with open('meta.txt','w',encoding='utf-8') as f:
                f.write(resp)
            await event.reply(file='meta.txt')
            os.remove('meta.txt')
        else:
            await event.reply(resp)

    except Exception as e:
        logger.error(f"İşleme hata: {e}")
        await event.reply(f"❌ Hata: {e}")
    finally:
        for _ in range(5):
            try:
                os.remove(path)
                break
            except PermissionError:
                await asyncio.sleep(1)
            except Exception:
                break

# Mesaj handler
@bot.on(events.NewMessage)
async def handler(event):
    if not event.is_private:
        return
    text = event.raw_text.strip().lower()
    if text == '/start':
        await event.reply(START_MESSAGE)
    elif text == '/help':
        await event.reply(HELP_MESSAGE)
    elif event.media:
        msg = await event.reply("📥 Dosya alındı, işleniyor...")
        stages = [
            "🔍 EXIF bilgi taranıyor...",
            "🔧 Metadata hazırlanıyor...",
            "⚙️ Teknik analiz yapılıyor...",
            "📤 Gönderim için hazırlanıyor..."
        ]
        for st in stages:
            await asyncio.sleep(1)
            await msg.edit(st)
        spinner = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
        for i in range(20):
            dot_count = (i % 4) + 1
            await msg.edit(f"⏳ Yükleniyor{'.' * dot_count} {spinner[i % len(spinner)]}")
            await asyncio.sleep(0.4)
        await process_media(event)
        await msg.delete()

if __name__ == '__main__':
    logger.info(f"Capi Info Bot v{VERSION} aktif 🚀")
    bot.run_until_disconnected()
