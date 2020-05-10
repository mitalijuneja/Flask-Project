
########
# Mitali Juneja (mj2944)
# Homework 5 = weather information
#
########

import pyowm

def get_temperature(city):
    """get temperature in input city"""
    
    key = 'f0ccb1103e28db3dae17b0818dff5b9d'
    owm = pyowm.OWM(key)
    weather = owm.weather_at_place(city)
    return round(weather.get_weather().get_temperature('fahrenheit')['temp'])




