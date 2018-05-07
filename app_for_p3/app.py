###################
##### Imports #####
###################

import pandas as pd
from flask import (Flask, render_template, jsonify, request)
from flask_uploads import UploadSet, DATA, configure_uploads

#######################
##### Flask setup #####
#######################

app = Flask(__name__)

##################
##### Routes #####
##################

# Render static webpages
@app.route('/')
def render_home_page():
    return render_template('index.html')

@app.route('/visualization')
def render_visualization_page():
    return render_template('visualization.html')

@app.route('/data1')
def render_data1_page():
    return render_template('data1.html')

@app.route('/data2')
def render_data2_page():
    return render_template('data2.html')

@app.route('/features')
def render_features_page():
    return render_template('/features.html')

@app.route('/diagnosis_app')
def render_app_page():
    return render_template('diagnosis_app.html')

if __name__ == '__main__':
    app.run(debug=True, port=5007)