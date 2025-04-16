
import tkinter as tk
import requests

API_KEY = "74a0e749a2c8400edf279a6d36b21f8a"
UNITS = "imperial"

def get_weather_by_city(city_query):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_query}&units={UNITS}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": data["main"]["temp"],
            "min_temp": data["main"]["temp_min"],
            "max_temp": data["main"]["temp_max"],
            "desc": data["weather"][0]["description"]
        }
    else:
        return None

def run_ui():
    def search():
        city_query = city_entry.get().strip()
        result_text.set("Searching...")
        weather = get_weather_by_city(city_query)
        if weather:
            result_text.set(f"City: {weather['city']}, {weather['country']}\n"
                            f"Temperature: {weather['temp']}°F\n"
                            f"Min Temperature: {weather['min_temp']}°F\n"
                            f"Max Temperature: {weather['max_temp']}°F\n"
                            f"Condition: {weather['desc'].title()}")
        else:
            result_text.set("City not found or API error.")

    root = tk.Tk()
    root.title("Simple Weather App")

    tk.Label(root, text="City (e.g. London,UK or Baltimore,MD,US):").grid(row=0, column=0, padx=10, pady=10)
    city_entry = tk.Entry(root, width=30)
    city_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(root, text="Get Weather", command=search).grid(row=1, column=0, columnspan=2)

    result_text = tk.StringVar()
    tk.Label(root, textvariable=result_text, justify="left").grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_ui()
