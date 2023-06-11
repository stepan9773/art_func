import os

from flask import Flask, request, render_template, jsonify
import json
import pandas as pd
import numpy as np
from get_angle import get_angle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    xb = int(request.form['Xb'])
    yb = int(request.form['Yb'])
    hb = int(request.form['Hb'])
    xc = int(request.form['Xc'])
    yc = int(request.form['Yc'])
    hc = int(request.form['Hc'])
    #xb = int(request.args.get('Xb'))
    #yb = int(request.args.get('Yb'))
    #hb = int(request.args.get('Hb'))
    #xc = int(request.args.get('Xc'))
    #yc = int(request.args.get('Yc'))
    #hc = int(request.args.get('Hc'))


    # Perform some calculations using the provided parameters
    result = get_angle(xb,yb,hb,xc,yc,hc)

    response = {
        'result': result
    }

    return json.dumps(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)