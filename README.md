Weather App (Tkinter Edition)
=============================

Overview
--------
This is a simple desktop weather application built with Python and Tkinter. It uses the OpenWeatherMap API to retrieve current weather data for any city in the world. The app supports precise queries using city, state, and country codes to avoid confusion with cities that share the same name.

Features
--------
1. Simple and clean graphical user interface using Tkinter
2. Input field for city names in the format: City or City,StateCode,CountryCode
3. Live weather data fetched directly from OpenWeatherMap API
4. Displays city name, country, temperature in Celsius, and weather condition

Requirements
------------
- Python 3.x
- Internet connection
- A valid OpenWeatherMap API key (already embedded in this example)

Installation
------------
1. Download the file `simple_weather_app.py`
2. Ensure you have Python 3 installed on your system
3. Open a terminal or command prompt
4. Navigate to the folder containing the Python file
5. Run the app using the command:

   python simple_weather_app.py

Usage
-----
1. Launch the application
2. In the input field, type the city you want to get weather for
   - For common cities, just the name is enough (e.g. London)
   - For more precise searches, use format: City,StateCode,CountryCode
     - Example: Baltimore,MD,US
     - Example: London,ON,CA
3. Click the 'Get Weather' button
4. The weather information will be displayed below, showing:
   - City and country
   - Current temperature in Fahrenheit
   - Minimum temperature in Fahrenheit
   - Maximum temperature in Fahrenheit
   - Humidity percentage
   - Weather condition (e.g. Clear sky, Rain)

Troubleshooting
---------------
- If the city is not found, make sure the spelling is correct and the location format follows the guidelines
- You must be connected to the internet for the API calls to work
- If the OpenWeatherMap API is unavailable or returns an error, try again later

License
-------
This project is for personal use and experimentation. No license or warranty is provided.

Author
------
Built by a Python enthusiast using VS Code and OpenWeatherMap API
'''
