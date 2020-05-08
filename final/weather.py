#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:03:29 2020

@author: mitalijuneja1
"""

import pyowm

def get_temperature(city):
    key = 'f0ccb1103e28db3dae17b0818dff5b9d'
    owm = pyowm.OWM(key)
    weather = owm.weather_at_place(city)
    return round(weather.get_weather().get_temperature('fahrenheit')['temp'])



# key = f0ccb1103e28db3dae17b0818dff5b9d
