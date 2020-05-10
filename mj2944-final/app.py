
########
# Mitali Juneja (mj2944)
# Final assignment = Flask app
#
########

#import statements
from flask import Flask, request, render_template
from stock_vis import get_data, calc_stats, plot_data
from weather import get_temperature
from image_search import get_image_url

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    """home route shows homepage with required information"""
    
    return render_template("index.html")


@app.route("/stock-visualizer")
def stock():
    """stock visualization route shows a form to input some stock information
    for this page"""
    
    return render_template("stock_form.html")

@app.route("/stock-visualizer", methods=["POST"])
def stock_post():
    """stock visualization route uses the input information to calculated some 
    information about the stock, generate a plot, and display it all in html"""
    
    symb = request.form["symbol"]
    date = request.form["purchase_date"]
    data, date = get_data(symb, date)
    stats = calc_stats(data, date)
    stats['symbol'] = symb
    plot_data(data, date, symb)
    return render_template("stock_vis.html", stats=stats)


@app.route("/weather")
def weather():
    """weather route shows a form to input a city"""
    
    return render_template("weather_form.html")


@app.route("/weather", methods=["POST"])
def weather_post():
    """weather route uses the input information to retrieve the current 
    temperature and a background image and display it all in html"""
    
    city = request.form["city"]
    get_image_url(city)
    data = {"city" : city.upper()}
    data["temp"] = str(get_temperature(city))
    return render_template("weather.html", data=data)

    


#start the server
if __name__ == "__main__":
    app.run()
    
