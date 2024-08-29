import requests

def hava_durumu_bilgileri_al(sehir):
    API_KEY = "YOUR_API_KEY"  # OpenWeatherMap API key'i buraya ekleyin
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        hava_durumu = data["weather"][0]["description"]
        sicaklik = data["main"]["temp"]
        nem_orani = data["main"]["humidity"]
        ruzgar_hizi = data["wind"]["speed"]
        print(f"{sehir} için Hava Durumu Bilgileri:")
        print(f"Hava Durumu: {hava_durumu}")
        print(f"Sıcaklık: {sicaklik} °C")
        print(f"Nem Oranı: {nem_orani}%")
        print(f"Rüzgar Hızı: {ruzgar_hizi} m/s")
    else:
        print("Hava durumu bilgileri alınamadı.")

if __name__ == "__main__":
    sehir = input("Hava durumu bilgilerini almak istediğiniz şehri girin: ")
    hava_durumu_bilgileri_al(sehir)
