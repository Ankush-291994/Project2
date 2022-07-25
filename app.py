
#from distutils.log import debug
from flask import Flask, render_template, request
import jsonify
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('attr_emp.pkl', 'rb'))


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    '''
    For direct API calls trought request
    '''
    Age = (request.form['Age'])
    StockOptionLevel=(request.form['StockOptionLevel'])
    RelationshipSatisfaction = (request.form['RelationshipSatisfaction'])
    TotalWorkingYears = (request.form['TotalWorkingYears'])
    WorkLifeBalance = (request.form['WorkLifeBalance'])
    YearsAtCompany = (request.form['YearsAtCompany'])
    YearsInCurrentRole = (request.form['YearsInCurrentRole'])
    OverTime_Yes = (request.form['OverTime_Yes'])
    prediction = model.predict([[Age, StockOptionLevel,RelationshipSatisfaction, TotalWorkingYears,
                               WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, OverTime_Yes]])

    output = prediction[0]
    return render_template("index.html", result=output)

# @app.route("/predict")
# def predict():
#     return render_template("index.html")
# def api_response():
#     from flask import jsonify
#     if request.method == 'POST':
#         return jsonify(**request.json)

if __name__ == '__main__':
    app.run(debug=True)
