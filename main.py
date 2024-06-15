import requests
import json
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=28ec9b2524094d0e90854833241506&q={city}"

r = requests.get(url)

if r.status_code == 200:
    wdic = r.json()
    temp_c = wdic["current"]["temp_c"]
    print(f"Current temperature in {city}: {temp_c}°C")

    speak(f"Current temperature in {city} is {temp_c} degrees Celsius.")
else:
    print(f"Error fetching data. Status code: {r.status_code}")
