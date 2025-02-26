from flask import Flask, request, jsonify
from data_collection import fetch_real_time_data
from model_inference import load_model, predict
import pandas as pd

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = fetch_real_time_data()
    return data.to_json()

@app.route('/predict', methods=['POST'])
def get_prediction():
    data = request.get_json()
    data_df = pd.DataFrame(data)
    model = load_model('model.pkl')
    prediction = predict(model, data_df)
    return jsonify(prediction=prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True)
