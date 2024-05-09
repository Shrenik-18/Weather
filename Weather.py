# -*- coding: utf-8 -*-
"""
Created on Wed May  8 23:53:23 2024

@author: jshre
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = "c5e497264650416eb12183120240805" 
    url = f"https://api.weatherapi.com/v1/current.json?key=c5e497264650416eb12183120240805&q=Bangalore&aqi=yes"
    response = requests.get(url)
    data = response.json()
    weather = {
        "city": city,
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description'],
        "icon": data['weather'][0]['icon']
    }
    return weather

@app.route('/')
def index():
    cities = ['Bangalore', 'Mumbai', 'Delhi']
    weather_data = [get_weather(city) for city in cities]
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
