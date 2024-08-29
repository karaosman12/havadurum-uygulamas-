# havadurum uygulaması


Bu Visual Studio projesi, Python ve OpenWeatherMap API'sini kullanarak belirtilen bir şehrin güncel hava durumu bilgilerini almayı sağlar. Uygulama, kullanıcının girdiği şehir adına göre hava durumu, sıcaklık, nem oranı ve rüzgar hızı gibi bilgileri ekrana yazdırır.

## Gereksinimler

- Python 3.x
- Visual Studio (Python geliştirme iş yükü yüklü)
- `requests` kütüphanesi (Eğer yüklü değilse, aşağıdaki komutla yükleyebilirsiniz)
- OpenWeatherMap API anahtarı

## Kurulum

1. **Proje Dosyasını Oluşturun:**

   - Visual Studio'da yeni bir Python projesi oluşturun.
   - Dosya adı olarak `hava_durumu.py` kullanabilirsiniz.

2. **Gerekli Python kütüphanesini yükleyin:**

   - Visual Studio'da, `Tools > Python > Python Environments` menüsünden Python ortamınızı seçin.
   - `pip install requests` komutunu kullanarak `requests` kütüphanesini yükleyin.

3. **OpenWeatherMap API Anahtarını Alın:**

   - OpenWeatherMap sitesine kaydolun ve bir API anahtarı alın.
   - `hava_durumu.py` dosyanızda, `API_KEY` değişkenine kendi API anahtarınızı ekleyin:

     ```python
     API_KEY = "YOUR_API_KEY"  # OpenWeatherMap API key'i buraya ekleyin
     ```

## Kullanım

1. **Kodu Çalıştırın:**

   - Visual Studio'da `hava_durumu.py` dosyanızı açın.
   - `Run` butonuna basarak veya `F5` tuşuna basarak kodu çalıştırın.

2. **Şehir Adını Girin:**

   - Program sizden hava durumu bilgilerini almak istediğiniz şehrin adını isteyecektir. Şehir adını girdikten sonra Enter tuşuna basın.

3. **Sonuçları Görüntüleyin:**

   - Girdiğiniz şehre ait hava durumu, sıcaklık, nem oranı ve rüzgar hızı gibi bilgiler ekranda görüntülenecektir.

## Örnek Çıktı

```plaintext
Hava durumu bilgilerini almak istediğiniz şehri girin: Istanbul
Istanbul için Hava Durumu Bilgileri:
Hava Durumu: clear sky
Sıcaklık: 25 °C
Nem Oranı: 60%
Rüzgar Hızı: 5 m/s
 
