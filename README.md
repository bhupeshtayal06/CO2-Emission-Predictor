# 🚗 CO₂ Emission Predictor App

A machine learning-powered Streamlit web app that predicts **vehicle CO₂ emissions** based on input parameters like engine size, cylinders, fuel type, and fuel consumption.

---

## 🎯 Objective
The goal of this project is to build a machine learning web application that predicts the CO2 emissions of a vehicle based on its specifications such as engine size, cylinders, fuel consumption, and more. This project aims to create awareness about vehicle pollution and assist users in understanding the environmental impact of their vehicles.

---

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

---

## 🧠 Machine Learning Models Used

- Linear Regression ✅ *(Best performing)*
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor (SVR)

---

📦 Input Parameters (Features)
Feature	Description
Engine Size	Size of the vehicle engine (L)
Cylinders	Number of engine cylinders
Transmission	Transmission type (e.g. A6, M5)
Fuel Type	Fuel used (e.g. Z, X, D, E)
Fuel Consumption	Average fuel usage (L/100km)

---