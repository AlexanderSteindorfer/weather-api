import requests
import datetime


def degree_to_direction(degree):
    """Converts wind degrees to wind direction.
    """
    if degree > 337.5: return 'Northerly'
    if degree > 292.5: return 'North Westerly'
    if degree > 247.5: return 'Westerly'
    if degree > 202.5: return 'South Westerly'
    if degree > 157.5: return 'Southerly'
    if degree > 122.5: return 'South Easterly'
    if degree > 67.5: return 'Easterly'
    if degree > 22.5: return 'North Easterly'
    return 'Northerly'


now = datetime.datetime.now()
time = now.strftime("%H:%M")
date_time = now.strftime("%m/%d/%Y, %H:%M")


API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&units=metric&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    
    wind_direction = degree_to_direction(data["wind"]["deg"])
 
    print("\nWeather in", data["name"].upper(), "(" + data["sys"]["country"] + "),", date_time + ":\n\n" 
            + str(int(data["main"]["temp"])), "°C",
            "|", data["weather"][0]["description"],
            "|", "wind:", int(float(data["wind"]["speed"]) * 3.6), "km/h", wind_direction, "\n")
else:
    print("An error occurred.")