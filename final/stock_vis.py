#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:20:59 2020

@author: mitalijuneja1
"""

'''
On your terminal run:
pip install alpha_vantage
This also uses the pandas dataframe, and matplotlib, commonly used python packages
pip install pandas
pip install matplotlib
For the develop version run:
pip install git+https://github.com/RomelTorres/alpha_vantage.git@develop
'''

from alpha_vantage.timeseries import TimeSeries
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import datetime





def get_data(symb, dt):
    date = format_date(dt)
    key = 'AR8Q3PVC72Z9J74R' 
    ts = TimeSeries(key, output_format='pandas')
    symb = symb.upper()
    data, meta = ts.get_daily_adjusted(symbol=symb, outputsize='full')
    return data, date

def calc_stats(data, dt):
    stats = {}
    stats['date'] = dt
    last_close = data.iloc[0]['4. close']
    purch_close = data.loc[dt]['4. close']
    stats['last close'] = last_close
    stats['purchase close'] = purch_close
    change = last_close - purch_close
    percent = change/purch_close * 100
    stats['change'] = change
    stats['percent'] = round(percent, 5)
    since_close = data.loc[:dt]['4. close']
    max_close = since_close.max()
    max_date = since_close.idxmax()
    stats['max close'] = round(max_close, 2)
    stats['max date'] = max_date
    stats['max change'] = max_close - purch_close
    stats['max percent'] = round(stats['max change']/purch_close * 100, 5)
    return stats
    
def format_date(dt):
   dt_el = dt.split("-")
   return datetime.datetime(int(dt_el[0]), int(dt_el[1]),int(dt_el[2]))

def plot_data(data, dt, symb):
    figure(num=None, figsize=(15,6), dpi=100, facecolor='w', edgecolor='k')
    data['4. close'].plot(color='#14213d', label="{} close".format(symb.upper()))
    plt.tight_layout()
    plt.grid()
    #check if it contains the purchase date otherwise move around days
    purch_close=data.loc[dt]['4. close']
    plt.axhline(y=purch_close, color='#fca311', linestyle='dashed', label='purchase price')
    plt.axvline(x=dt, color='#fca311', linestyle='dashed', label='purchase date')
    plt.legend()
    plt.savefig(fname='static/stock_plot.png')


data, date = get_data('AAPL', "2019-05-03")
print(calc_stats(data, date))
plot_data(data, date, 'aapl')