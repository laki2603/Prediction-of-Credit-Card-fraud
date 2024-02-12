import numpy as np
import pandas as pd
import  pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    data = [d for d in request.form.values()]
    features = [np.array(data)]
    prediction = model.predict(features)
    if int(prediction[0]) == 1:
        return render_template("index.html", prediction_text="This is a fraud transaction")
    else:
        return render_template("index.html", prediction_text="This is a legit transaction")

@app.route("/predict_api", methods = ["POST"])
def predict_api():
    json_data = request.get_json()
    re_df = pd.DataFrame([json_data])
    prediction = model.predict(re_df)
    return jsonify({"Prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)