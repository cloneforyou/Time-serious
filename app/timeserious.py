from datetime import datetime
from flask import Flask, render_template,request,redirect,session,jsonify
import simplejson as json
import pandas
import csv
import analyse

app = Flask(__name__,static_url_path='')


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/addData',methods=['POST'])
def addData():
    try:
        _url = request.form['urlInput']
        _source = request.form['dataSource']
        _units = request.form['selectUnits']
        _entity = request.form['entityName']

        # results = json.dumps({'url':_url,'source':_source,'units':_units,'entity':_entity})

        if _url and _source and _units:
            if _units == 'tonnes of CO2 equivalent gas':
                #blah
                results = analyse.analyseData(_url,_source,_units,_entity)
                # print allresults
                return render_template('emissions2.html', results=results,units=_units,source=_source,entity=_entity)

            if _units == 'dollars':
                #blah
                results = analyse.analyseData(_url,_source,_units,_entity)
                # print allresults
                return render_template('emissions2.html', results=results,units=_units,source=_source,entity=_entity)    

    except Exception as e:
        return render_template('error.html',error = str(e))

if __name__ == '__main__':
    app.run(debug=True)