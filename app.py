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
@app.route('/visualization')
def render_visualization_page():
    return render_template('visualization.html')

@app.route('/data1')
def render_data1_page():
    return render_template('data1.html')

@app.route('/data2')
def render_data1_page():
    return render_template('data2.html')

@app.route('/features')
def render_template():
    return render_template('/features.html')