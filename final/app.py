# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, request, render_template
from stock_vis import get_data, calc_stats, plot_data
from weather import get_temperature
from image_search import get_image_url, save_image

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/stock-visualizer")
def stock():
    return render_template("stock_form.html")

@app.route("/stock-visualizer", methods=["POST"])
def stock_post():
    symb = request.form["symbol"]
    date = request.form["purchase_date"]
    data, date = get_data(symb, date)
    stats = calc_stats(data, date)
    stats['symbol'] = symb
    plot_data(data, date, symb)
    return render_template("stock_vis.html", stats=stats)

@app.route("/weather")
def weather():
    return render_template("weather_form.html")

@app.route("/weather", methods=["POST"])
def weather_post():
    city = request.form["city"]
    get_image_url(city)
    #save_image(url)
    data = {"city" : city.upper()}
    data["temp"] = str(get_temperature(city))
    return render_template("weather.html", data=data)
    
@app.route("/miku")
def miku():
    return "Hi Miku!"

#start the server
if __name__ == "__main__":
    app.run()
    
#client id = 867595989023-8do0vdup84d3iu4u9oiujdhnqs7cf8pp.apps.googleusercontent.com
#client secret = AnD8mRmIdNP0KQNj8E4FV4q2