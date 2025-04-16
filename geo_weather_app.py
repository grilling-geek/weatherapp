import tkinter as tk
import requests

API_KEY = "74a0e749a2c8400edf279a6d36b21f8a"
UNITS = "imperial"

def get_location_data(city_query):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_query}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return {
                "name": data[0].get("name", ""),
                "lat": data[0]["lat"],
                "lon": data[0]["lon"],
                "state": data[0].get("state", ""),
                "country": data[0]["country"]
            }
    return None

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?units={UNITS}&lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "min_temp": data["main"]["temp_min"],
            "max_temp": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "desc": data["weather"][0]["description"]
        }
    return None

def run_ui():
    def search():
        city_query = city_entry.get().strip()
        result_text.set("Looking up location...")
        location = get_location_data(city_query)
        if not location:
            result_text.set("City not found.")
            return

        result_text.set("Fetching weather data...")
        weather = get_weather(location["lat"], location["lon"])
        if weather:
            full_name = f"{location['name']}, {location['state']}, {location['country']}".strip(', ')
            result_text.set(f"Location: {full_name}\n"
                            f"Temperature: {weather['temp']}°F\n"
                            f"Min Temperature: {weather['min_temp']}°F\n"
                            f"Max Temperature: {weather['max_temp']}°F\n"
                            f"Humidity: {weather['humidity']}%\n"
                            f"Condition: {weather['desc'].title()}")
        else:
            result_text.set("Weather data not found.")

    root = tk.Tk()
    root.title("Weather App with Location Info")

    tk.Label(root, text="City (e.g. Paris,TX,US):").grid(row=0, column=0, padx=10, pady=10)
    city_entry = tk.Entry(root, width=30)
    city_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(root, text="Get Weather", command=search).grid(row=1, column=0, columnspan=2)

    result_text = tk.StringVar()
    tk.Label(root, textvariable=result_text, justify="left").grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_ui()