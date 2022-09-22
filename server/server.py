from flask import Flask, request, jsonify
import util
import math

estimated_price = None


app = Flask(__name__)

@app.route('/get_model_names', methods=['GET'])
def get_model_names():


    response = jsonify({
        'models': util.get_model_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_car_price', methods=['GET', 'POST'])
def predict_car_price():

    km_driven = round(float(request.form['km_driven']))
    model = request.form['model']
    car_age = float(request.form['car_age'])
    owner = int(request.form['owner'])


    response = jsonify({
        'estimated_price': util.get_estimated_price(model,km_driven,owner,car_age)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()
