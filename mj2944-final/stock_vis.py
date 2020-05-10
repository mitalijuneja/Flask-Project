
#########
# Mitali Juneja (mj2944)
# Homework 5 = stock visualizer functionality
#
#########

from alpha_vantage.timeseries import TimeSeries
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import datetime





def get_data(symb, dt):
    """properly format the input information (capitalization, convert to 
    datetime object)"""
    
    date = format_date(dt)
    key = 'AR8Q3PVC72Z9J74R' 
    ts = TimeSeries(key, output_format='pandas')
    symb = symb.upper()
    data, meta = ts.get_daily_adjusted(symbol=symb, outputsize='full')
    return data, date


def calc_stats(data, dt):
    """calculate some basic information from the closing column of the 
    timeseries pandas dataframe, return as a dictionary to display in html"""
    
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
   """convert input date to datetime object and fix weekend dates to weekday
   dates"""
    
   dt_el = dt.split("-")
   date = datetime.datetime(int(dt_el[0]), int(dt_el[1]),int(dt_el[2]))
   # make Saturdays into Fridays
   if date.weekday() == 5:
       date = date - datetime.timedelta(days=1)
   # make Sundays into Mondays
   if date.weekday() == 6:
       date = date + datetime.timedelta(days=1)
   return date


def plot_data(data, dt, symb):
    """plot the timeseries data with matplotlib and save"""
    
    figure(num=None, figsize=(15,6), dpi=100, facecolor='w', edgecolor='k')
    data['4. close'].plot(color='#14213d', label="{} close".format(symb.upper()))
    plt.tight_layout()
    plt.grid()
    purch_close=data.loc[dt]['4. close']
    plt.axhline(y=purch_close, color='#fca311', linestyle='dashed', label='purchase price')
    plt.axvline(x=dt, color='#fca311', linestyle='dashed', label='purchase date')
    plt.legend()
    plt.savefig(fname='static/stock_plot.png')


