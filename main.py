'''
Main script for application
'''

from datetime import datetime
from pytz import timezone
from flask import Flask, render_template

# for scraper use
import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

url = "https://greatday.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
quote_from_greatday = soup.find(id="theQuote")
print(type(quote_from_greatday))
print("convert bs4.element.tag object to str object")
quote_string = quote_from_greatday.text
print(type(quote_string))
print("Quote from greatday.com received")
print("-----------")
print(quote_from_greatday)
print("-----------")

tz = timezone("US/Eastern")
time = datetime.now(tz)
year = time.year
month = time.month
day = time.day
hour = time.hour
minutes = time.minute

yymmdd = "{}/{}/{} {}:{}".format(str(year), str(month), str(day), str(hour), str(minutes))

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homepage.html', datetime=yymmdd)

@app.route('/about')
def about():
    return render_template('about.html', datetime=yymmdd)

@app.route('/essays/why_I_began_coding')
def why_I_began_coding():
    return render_template('why_I_began_coding.html')

@app.route("/data", methods=['POST', 'GET'])
def data():
    return render_template("quote.html", quote=quote_string)