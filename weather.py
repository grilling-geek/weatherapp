import requests # type: ignore


class City:
    def __init__(self, name, lat, lon, units = "imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:

            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=74a0e749a2c8400edf279a6d36b21f8a")

        except:

            print("No internet access")

        self.response_json = response.json()
        self.name = self.response_json["name"]
        self.temp = self.response_json ["main"]["temp"]
        self.temp_min = self.response_json ["main"]["temp_min"]
        self.temp_max = self.response_json ["main"]["temp_max"]
        self.country = self.response_json["sys"]["country"]

    def temp_print(self):
        #units_symbol = "F"
        if self.country == "US":
            units_symbol = "F"
        else: 
            units_symbol = "C"
        print(f"In {self.name}, {self.country}, it is {self.temp}°{units_symbol}. Today's high is {self.temp_max}°{units_symbol} with a low of {self.temp_min}°{units_symbol}")

my_city = City("", 25.761681, -80.191788)
my_city.temp_print()
#print(my_city.response_json)

vacation_city =  City("", 30.311876, -95.456055)    
vacation_city.temp_print()   
#print(vacation_city.response_json)