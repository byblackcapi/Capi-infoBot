# Capi Info Bot 🚀

![Python](https://img.shields.io/badge/python-3.7%2B-blue) ![Version](https://img.shields.io/badge/version-1.5.5-green)

**Capi Info Bot** Telegram üzerinden gönderdiğiniz medya dosyalarınızın EXIF ve teknik metadata bilgilerini hızlıca çıkarmanızı sağlayan bir bottur.

---

## Özellikler

* 📸 **EXIF Bilgileri**: Fotoğraflarınızın kamera markası, model, çekim zamanı, enstantane, diyafram, ISO ve daha fazlasını gösterir.
* 🌍 **GPS Konumu**: EXIF içindeki GPS bilgileri varsa enlem ve boylam değerlerini alır, Google Maps bağlantısı sunar.
* 🔒 **Hash Hesaplama**: Dosyanızın SHA256 ve MD5 hash değerlerini hesaplar.
* 🗃️ **Teknik Metadata**: `hachoir` kütüphanesi ile medya dosyalarının detaylı teknik metadata bilgilerini alır.
* ⚙️ **Otomatik Temizleme**: İşlem sonrası geçici dosyaları temizler.
* 🔄 **Asenkron İşlem**: Hızlı ve kesintisiz kullanıcı deneyimi için tüm işlemler asenkron olarak yürütülür.

## Gereksinimler

* Python 3.7 veya üzeri
* Telegram bot hesabı (Bot Token)
* Aşağıdaki Python paketleri:

  ```bash
  pip install telethon pillow piexif exifread hachoir
  ```

## Kurulum

1. Bu depoyu klonlayın:

   ```bash
   git clone https://github.com/<kullanici_adiniz>/capi-info-bot.git
   cd capi-info-bot
   ```
2. Sanal ortam oluşturun ve etkinleştirin (isteğe bağlı):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\\Scripts\\activate   # Windows
   ```
3. Gerekli paketleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```
4. `config.py` dosyasını oluşturun ve aşağıdaki değerleri düzenleyin:

   ```python
   API_ID = 23350184
   API_HASH = '41f0c2a157268e158f91ab7d59f4fc19'
   BOT_TOKEN = '7619515923:AAGlzmlklTqP3OXH-tgbdR3KHVEnwP0BZqc'
   ```

## Kullanım

```bash
python bot.py
```

Telegram’da botunuzu başlatın ve aşağıdaki komutları kullanın:

* `/start` - Botu başlatır ve giriş mesajını gönderir.
* `/help`  - Yardım metnini gösterir.
* **Medya Gönderme** - Fotoğraf, video veya belge gönderin; bot metadata bilgilerini size iletir.

İşlem adımları:

1. Dosyanız indiriliyor.
2. EXIF bilgileri taranıyor.
3. Hash ve dosya sistemi metadata hazırlanıyor.
4. `hachoir` ile teknik analiz yapılıyor.
5. Sonuçlar size mesaj veya `.txt` dosyası olarak gönderiliyor.

## Özelleştirme

* `VERSION` değişkenini güncelleyerek bot sürümünü takip edebilirsiniz.
* `stages` listesinde yer alan yükleme mesajlarını ihtiyacınıza göre değiştirebilirsiniz.
* Çıktı formatını `process_media` fonksiyonunda düzenleyerek farklı bilgileri ekleyebilir veya çıkarabilirsiniz.

## Katkıda Bulunma

1. Fork’layın.
2. Yeni bir branch oluşturun: `git checkout -b feature/yenilik`.
3. Değişikliklerinizi commit edin: `git commit -m 'Yeni özellik eklemesi'`.
4. Branch’e push edin: `git push origin feature/yenilik`.
5. Pull request oluşturun.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakınız.

---

> **Not:** API kimlik bilgilerinizi herkese açık bir repoda paylaşmamaya dikkat edin! `config.py` dosyasını `.gitignore` dosyanıza eklemeniz önerilir.
