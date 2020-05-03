# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, request, render_template
from stock_vis import get_data, calc_stats, plot_data

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/stock-visualizer")
def engi():
    return render_template("stock_form.html")

@app.route("/stock-visualizer", methods=["POST"])
def engi_post():
    symb = request.form["symbol"]
    date = request.form["purchase_date"]
    data, date = get_data(symb, date)
    stats = calc_stats(data, date)
    stats['symbol'] = symb
    plot_data(data, date, symb)
    return render_template("stock_vis.html", stats=stats)

@app.route("/miku")
def miku():
    return "Hi Miku!"

#start the server
if __name__ == "__main__":
    app.run()