from datetime import datetime
from pytz import timezone
from flask import Flask, render_template

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