import requests
import PySimpleGUI as sg
from datetime import datetime

API_KEY = 'acd87c5cbd2dc901c76488e7c5f2695d'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    try:
        complete_url = BASE_URL + 'q=' + city + '&appid=' + API_KEY
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main_data = data["main"]
            temperature = main_data["temp"]
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            feels_like = main_data["feels_like"]

            weather_data = data["weather"]
            weather_description = weather_data[0]["description"]

            coord_data = data["coord"]
            latitude = coord_data["lat"]
            longitude = coord_data["lon"]

            timestamp = data["dt"]
            city_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            return f"Weather in {city}:\n" \
                    f"Temperature: {temperature}K\n" \
                    f"Pressure: {pressure}hPa\n" \
                    f"Humidity: {humidity}%\n" \
                    f"Description: {weather_description.capitalize()}\n" \
                    f"Feels-Like: {feels_like}K\n" \
                    f"Latitude: {latitude}\n" \
                    f"Longitude: {longitude}\n" \
                    f"Date and Time: {city_time}"
        else:
            return "City not found"

    except Exception as e:
        return f"An error occurred: {str(e)}"

sg.theme("LightGrey1")

layout = [
    [sg.Text("Enter city name:"), sg.InputText(key="CITY")],
    [sg.Button("Get Weather")],
    [sg.Text(size=(60, 15), key="OUTPUT")],
]

window = sg.Window("Weather App", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Get Weather":
        city_name = values["CITY"]
        result = get_weather(city_name)
        window["OUTPUT"].update(result)

window.close()
