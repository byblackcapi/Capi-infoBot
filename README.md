# 🚀 Capi Info Bot v1.5.5

![Capi Info Bot Logo](https://raw.githubusercontent.com/yourusername/capi-info-bot/main/logo.png)

Capi Info Bot, Telegram üzerinde medya dosyalarınızın EXIF, dosya sistemi metadata, detaylı teknik metadata ve hash bilgilerini hızlıca elde etmenizi sağlayan güçlü bir Telegram botudur.

---

## 📌 Özellikler

* 🔍 **EXIF Bilgileri**: Fotoğraf ve görsellerin kameraya özel meta verilerini (Make, Model, LensModel, ExposureTime vb.) çıkarır.
* 🗃️ **Teknik Metadata**: `hachoir` kütüphanesi ile video, belgeler ve diğer dosyaların derinlemesine teknik bilgisini çeker.
* 🔒 **Hash Hesaplama**: SHA256 ve MD5 hash değerlerini hesaplayarak dosya bütünlüğünü doğrular.
* 🌐 **Konum Desteği**: EXIF GPS verilerini okuyup Google Maps linki oluşturur.
* ⚙️ **Kolay Kurulum**: Python ve gerekli kütüphanelerle birkaç adımda aktif edin.
* ✨ **Asenkron İşlem**: `asyncio` ile hızlı ve sorunsuz medya işlemleri.

---

## 📥 Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/yourusername/capi-info-bot.git
   cd capi-info-bot
   ```
2. Sanal ortam oluşturma (isteğe bağlı):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\\Scripts\\activate
   ```
3. Gerekli paketleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Yapılandırma

Ayarlar `index.py` dosyasında yer alır. Botu kendi bilgilerinle çalıştırmak için aşağıdaki değişkenleri `index.py` içinde güncelleyin:

| Değişken    | Açıklama                |
| ----------- | ----------------------- |
| `API_ID`    | Telegram API ID’niz     |
| `API_HASH`  | Telegram API Hash’ınız  |
| `BOT_TOKEN` | Telegram Bot Token’ınız |
| `VERSION`   | Bot sürüm bilgisi       |

Örnek ayarlar (`index.py` içinden):

```python
API_ID = 23350184
API_HASH = '41f0c2a157268e158f91ab7d59f4fc19'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
VERSION = '1.5.5'
```

\---------------|--------------------------|
\| `API_ID`      | Telegram API ID’niz      |
\| `API_HASH`    | Telegram API Hash’ınız   |
\| `BOT_TOKEN`   | Telegram Bot Token’ınız  |
\| `VERSION`     | Bot sürüm bilgisi        |

Örnek `.env`:

```

---

## 🚀 Kullanım

1. Botu başlatın:

   ```bash
   python bot.py
   ```
2. Telegram’dan botunuza `/start` komutunu gönderin.
3. Fotoğraf, video veya belge gönderin.
4. Bot size detaylı metadata ve hash bilgilerini gönderir.

### 🎛️ Komutlar

| Komut    | Açıklama                       |
| -------- | ------------------------------ |
| `/start` | Başlatma mesajını gösterir     |
| `/help`  | Yardım metnini tekrar gönderir |

---

## 🤝 Katkıda Bulunma

1. Fork’layın 🔱
2. Yeni bir branch açın: `git checkout -b feature/isim`
3. Değişikliklerinizi commit edin: `git commit -m 'Yeni özellik ekle'`
4. Push edin: `git push origin feature/isim`
5. Pull request açın 📨

---

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

---

> **Not:** 🚧 Herhangi bir sorun, öneri veya geri bildirim için [issues](https://github.com/yourusername/capi-info-bot/issues) bölümüne yazabilirsiniz. 🎉
