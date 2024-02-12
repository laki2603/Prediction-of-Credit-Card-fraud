# 💳 Credit Card Fraud Detection Flask API

This repository contains a Flask API for credit card fraud detection using a machine learning model. The project includes pre-trained models, data preprocessing, and an API for making predictions. Below, you'll find information on how to use this code for local development, the project structure.

# Local setup
- Used can either download or clone the code
- open command prompt and navigate to the folder where you have stored the downloaded/cloned file open src
- used the command `python app.py`
- the above command will run the app
- use this url after you run tghe app `http://127.0.0.1:5000/`

# Snippet of the application
![AppLication](https://github.com/laki2603/Prediction-of-Credit-Card-fraud/assets/72691874/10488d00-40d3-4048-a7f3-927e54be71b2)




# Project Structure
src - contains the code
src/Prediction_of_CreditCard%20_fraud.ipynb - The code which has my analysis and model building
src/model.pkl - A pickle file used for creading app
src/app.py - A file where I had created a app using flask
src/templates.index.html - Html file needed for frontend of my app
src/static/styles.css - Has the css changes used for the app
input - contains the screenshot and csv file

# Versions used in this project
Recomended to used this version if not some custom changes required from your side
scikit-learn 1.4.0
Python 3.11.4
pandas 1.5.3
