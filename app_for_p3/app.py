###################
##### Imports #####
###################

import os
import pandas as pd
from flask import (Flask, render_template, jsonify, request)
from flask_uploads import UploadSet, DATA, configure_uploads

from sklearn.preprocessing import StandardScaler
from keras.models import load_model


#######################
##### Flask Setup #####
#######################

app = Flask(__name__)

app.config['UPLOADED_CSVS_DEST'] = 'static/uploads'
csvs = UploadSet('csvs', ('csv'))
configure_uploads(app, (csvs))

##################
##### Routes #####
##################

# Let user upload file
@app.route('/diagnosis_app', methods=['GET', 'POST'])
def diagnosis_app():
    if request.method == 'POST' and 'uploaded_csv' in request.files:
        csvs.save(request.files['uploaded_csv'], name='diagnosis_data.csv')
        return render_template('diagnosis_results.html')
    return render_template('diagnosis_app.html')

# Return prediction data
@app.route('/model_predict')
def model_predict():
    # Format input file to right dimensions
    input_df = pd.read_csv('static/uploads/diagnosis_data.csv')
    X_input = input_df.drop('ID number', axis=1)

    # Scale X_input with the original X_train used to train the model
    X_train = pd.read_csv('static/modeling/X_train.csv')
    X_scaler = StandardScaler().fit(X_train)
    X_input_scaled = X_scaler.transform(X_input)

    # Load model and predict
    model = load_model('static/modeling/diagonsis_model_10000.h5')
    predictions = predictions = model.predict_classes(X_input_scaled).tolist()

    # Format predictions to string
    predictions_str = []
    for prediction in predictions:
        if prediction == 0:
            predictions_str.append('Benign')
        else:
            predictions_str.append('Malignant')

    # Prepare data for export
    output_dict = {
        'sample_id': input_df['ID number'].tolist(),
        'prediction': predictions_str
    }

    # Clear uploads directory for next input
    os.remove('static/uploads/diagnosis_data.csv')

    return jsonify(output_dict)



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

@app.route('/diagnosis_results')
def render_results_page():
    return render_template('diagnosis_results.html')

if __name__ == '__main__':
    app.run(debug=True, port=5011)