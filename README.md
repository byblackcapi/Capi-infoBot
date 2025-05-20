# 🚀 Capi Info Bot v1.5.5

![Capi Info Bot Logo](https://raw.githubusercontent.com/byblackcapi/Capi-infoBot/main/infobot.png)

**Capi Info Bot**, Telegram üzerinde medya dosyalarınızın EXIF, dosya sistemi metadata, detaylı teknik metadata ve hash bilgilerini kolayca almanızı sağlayan şık ve hızlı bir bottur.

---

## 📌 Özellikler

* 🔍 **EXIF Bilgileri**: Make, Model, LensModel, ExposureTime, FNumber ve daha fazlasını çıkarır.
* 🗃️ **Teknik Metadata**: `hachoir` ile video, belge ve diğer dosyalara dair derinlemesine bilgi sağlar.
* 🔒 **Hash Hesaplama**: SHA256 ve MD5 hash değerleriyle dosya bütünlüğünü onaylar.
* 🌐 **Konum Desteği**: GPS verilerini okuyup anında Google Maps bağlantısı oluşturur.
* ✨ **Asenkron İşlem**: `asyncio` desteğiyle hızlı ve kesintisiz işlem süreci.
* ⚙️ **Kolay Kurulum**: Basit adımlarla hemen çalışır hale gelir.

---

## 📥 Kurulum

1. Repo’yu klonlayın:

   ```bash
   git clone https://github.com/yourusername/capi-info-bot.git
   cd capi-info-bot
   ```
2. (İsteğe bağlı) Sanal ortam oluşturup aktif edin:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Gereksinimleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Yapılandırma

Tüm ayarlar `index.py` dosyasında bulunur. Aşağıdaki değişkenleri kendi değerlerinizle güncelleyin:

| Değişken    | Açıklama                  |
| ----------- | ------------------------- |
| `API_ID`    | Telegram API ID’niz       |
| `API_HASH`  | Telegram API Hash’ınız    |
| `BOT_TOKEN` | Telegram Bot Token’ınız   |
| `VERSION`   | Bot sürümü (örn. '1.5.5') |

**Örnek `index.py`:**

```python
API_ID    = 23350184
API_HASH  = '41f0c2a157268e158f91ab7d59f4fc19'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
VERSION   = '1.5.5'
```

---

## 🚀 Kullanım

1. Botu çalıştırın:

   ```bash
   python index.py
   ```
2. Telegram’da botunuza `/start` gönderin.
3. Fotoğraf, video veya belge paylaşın.
4. Bot size tüm metadata ve hash bilgilerini gönderir.

### 🎛️ Komutlar

| Komut    | Açıklama                                            |
| -------- | --------------------------------------------------- |
| `/start` | Botu başlatır ve hoş geldiniz mesajı gösterir       |
| `/help`  | Komut listesini ve kullanım bilgisini tekrar yollar |

---

## 🤝 Katkıda Bulunma

1. Reposu fork’layın ⭐️
2. Yeni bir branch açın:

   ```bash
   git checkout -b feature/yenilik
   ```
3. Değişikliklerinizi commit edin:

   ```bash
   git commit -m 'Yeni özellik ekle'
   ```
4. Branch’i push’layın:

   ```bash
   git push origin feature/yenilik
   ```
5. Pull request açın 📣

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

> \:bulb: Sorun mu var? [Issues sayfasına](https://github.com/yourusername/capi-info-bot/issues) bekleriz! 🎉
