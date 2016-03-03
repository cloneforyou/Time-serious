from datetime import datetime
from flask import Flask, render_template, json, request,redirect,session,jsonify
import simplejson as simpljson
import pandas
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/the-time')
def the_time():
     cur_time = str(datetime.now())
     return cur_time + ' is the current time!  ...YEAH!'

if __name__ == '__main__':
    app.run(debug=True)