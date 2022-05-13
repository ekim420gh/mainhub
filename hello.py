import time
from flask import Flask, render_template

t = time.strftime("%I:%M %p")
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homepage.html', utc_dt=t)