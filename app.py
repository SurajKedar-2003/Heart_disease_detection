import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('HDPindex.html')

@app.route('/predict', methods = ['POST'])
def predict():
    age = float(request.form['age'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    thalach = float(request.form['thalach'])
    oldpeak = float(request.form['oldpeak'])

    
    sex_value = int(request.form['sex_0'])
    cp_value = int(request.form['cp_0'])
    fbs_value = int(request.form['fbs_0'])
    restecg_value = int(request.form['restecg_0'])
    exang_value = int(request.form['exang_0'])
    slope_value = int(request.form['slope_0'])
    ca_value = int(request.form['ca_0'])
    thal_value = int(request.form['thal_1'])


    sex_0 = 1 if sex_value == 0 else 0
    sex_1 = 1 if sex_value == 1 else 0
    
    
    cp_0 = 1 if cp_value == 0 else 0
    cp_1 = 1 if cp_value == 1 else 0
    cp_2 = 1 if cp_value == 2 else 0
    cp_3 = 1 if cp_value == 3 else 0

    fbs_0 = 1 if fbs_value == 0 else 0
    fbs_1 = 1 if fbs_value == 1 else 0          ##

    restecg_0 = 1 if restecg_value == 0 else 0
    restecg_1 = 1 if restecg_value == 1 else 0
    restecg_2 = 1 if restecg_value == 2 else 0

    exang_0 = 1 if exang_value == 0 else 0
    exang_1 = 1 if exang_value == 1 else 0

    slope_0 = 1 if slope_value == 0 else 0
    slope_1 = 1 if slope_value == 1 else 0
    slope_2 = 1 if slope_value == 2 else 0

    ca_0 = 1 if ca_value == 0 else 0
    ca_1 = 1 if ca_value == 1 else 0
    ca_2 = 1 if ca_value == 2 else 0

    thal_1 = 1 if thal_value == 1 else 0
    thal_2 = 1 if thal_value == 2 else 0
    thal_3 = 1 if thal_value == 3 else 0





    input_features = {
        "age": age,
        "trestbps": trestbps,
        "chol": chol,
        "thalach": thalach,
        "oldpeak": oldpeak,
        "sex_0": sex_0,
        "sex_1": sex_1,
        "cp_0": cp_0,
        "cp_1": cp_1,
        "cp_2": cp_2,
        "fbs_0": fbs_0,
        "fbs_1": fbs_1,
        "restecg_0": restecg_0,
        "restecg_1": restecg_1,
        "restecg_2": restecg_2,
        "exang_0": exang_0,
        "exang_1": exang_1,
        "slope_0": slope_0,
        "slope_1": slope_1,
        "slope_2": slope_2,
        "ca_0": ca_0,
        "ca_1": ca_1,
        "ca_2": ca_2,
        "thal_1": thal_1,
        "thal_2": thal_2,
        "thal_3": thal_3
    }
    df = pd.DataFrame([input_features])
    output = model.predict(df)

    if output==1:
        res_val = "heart disease"
    else:
        res_val = "no heart disease"
    
    return render_template('HDPindex.html', prediction_text = 'patient has {}'.format(res_val))

    if __name__ == "__main__":
        app.run(debug == True)