from flask import Flask, render_template, redirect, url_for, request
from forms import BreastCancerForm, ThyroidForm, FetalHealthForm
from calculate import ConvertToArray
import pickle
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = '4d2771bfcca7ddada03c739fb514ea1f'


def predict(form_values):
    # for breast cancer
    if len(form_values) == 30:
        flag = 1
        model = pickle.load(open('models/breast_cancer_model.pkl', 'rb'))
        return flag, model.predict(form_values.reshape(1,-1))[0]
    # for fetal health
    elif len(form_values) == 21:
        flag = 2
        model = pickle.load(open('models/fetal_health_model.pkl', 'rb'))
        return flag, model.predict(form_values.reshape(1,-1))[0]
    # for thyroid
    elif len(form_values) == 25:
        flag = 3
        model = pickle.load(open('models/thyroid_checking.pkl', 'rb'))
        return flag, model.predict(form_values.reshape(1,-1))[0]


@app.route('/')
def home():
    return render_template('home.html', title='Index Page')

@app.route('/breast_cancer', methods=['GET', 'POST'])
def breastCancer():
    form = BreastCancerForm()
    return render_template('breast_cancer.html', title='Breast Cancer Detection', form=form)

@app.route('/thyroid_checking', methods=['GET', 'POST'])
def thyroidChecking():
    form = ThyroidForm()
    return render_template('thyroid_checking.html', title='Thyroid Checking', form=form)

@app.route('/fetal_health', methods=['GET', 'POST'])
def fetalHealthDetect():
    form = FetalHealthForm()
    return render_template('fetal_health.html', title='Fetal Health', form=form)

@app.route('/prediction', methods=['POST', 'GET'])
def predictionPage():
    
    conversion = ConvertToArray()
    try:
        if request.method == 'POST':
            to_predict_data = request.form.to_dict()
            remove_csrf = to_predict_data.pop('csrf_token')
            remove_submit = to_predict_data.pop('submit')
            for k, v in to_predict_data.items():
                to_predict_data[k] = float(v)
    except:
        message = "Please Enter valid data"
        return render_template('home.html', title='Index Page', message=message)
    
    
    complete_array = conversion.dictToArray(to_predict_data)
    # print(len(complete_array))

    flag_value, pred = predict(complete_array)
    # print(flag_value)
    # print(pred)
    max_pred = np.argmax(pred)

    # it holds the percentage
    # chances = pred[max_pred]
    return render_template('prediction_page.html', title='Predict', pred=pred, max_pred = max_pred, flag_value=flag_value)

if __name__ == '__main__':
    app.run(debug=True, port=8080)


#! Till now, 3 disease are done (Breast Cancer, Fetal Health, Thyroid)
#* Create a function and send the array and check whether it is working or not
