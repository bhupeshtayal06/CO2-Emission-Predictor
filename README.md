# 🚗 CO₂ Emission Predictor App

A machine learning-powered Streamlit web app that predicts **vehicle CO₂ emissions** based on input parameters like engine size, cylinders, fuel type, and fuel consumption.

---

![Streamlit App Screenshot](streamlit app screenshot.png) 

## 🔗 Live Demo

🌐 Try the app here: [CO₂ Emission Predictor](https://bhupeshtayal06-co2-emission-predictor-app-ott1xl.streamlit.app/)

---

## 📌 Features

- 🔍 Predicts **CO₂ emissions** based on engine & fuel details
- 📊 Trained using **Linear Regression** for best accuracy
- 💡 Clean and intuitive **Streamlit** interface
- 🧠 Supports fast predictions with **pre-trained model**
- 📁 Code and models are well-organized for easy updates

---

## 📂 Project Structure

```
CO2-Emission-Predictor/
├── app.py
├── README.md
├── requirements.txt
│
├── .devcontainer/
│   └── devcontainer.json
│
├── assets/
│   └── streamlit app screenshot.png
│
├── datasets/
│   ├── emission.csv
│   └── FuelConsumption (1).csv
│
├── models/
│   ├── decision_tree_regressor.ipynb
│   ├── linear_regression.ipynb
│   ├── model.ipynb
│   ├── random_forest_regressor.ipynb
│   └── Support_Vector_Regressor.ipynb
│
└── saved_models/
    ├── columns.pkl
    ├── lr_model.pkl
    └── scaler.pkl

```