#🌦️ Simple Weather App

import requests

print("=== Simple Weather Checker ===")

city = input("Enter your city name: ").strip()

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    data = response.json()

    temp = data["current_condition"][0]["temp_C"]
    feels = data["current_condition"][0]["FeelsLikeC"]
    desc = data["current_condition"][0]["weatherDesc"][0]["value"]

    print("\n--- Weather Report ---")
    print("City:", city.title())
    print("Temperature:", temp, "°C")
    print("Feels Like:", feels, "°C")
    print("Condition:", desc)

except:
    print("Error getting weather. Check internet or city name.")
