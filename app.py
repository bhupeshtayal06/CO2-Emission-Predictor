import streamlit as st
import pickle
import numpy as np

# Title
st.title("CO2 Emission Prediction App 🚗💨")
st.markdown("Predict how much CO2 your vehicle will emit based on specs.")

# Load model, scaler, and column names
model = pickle.load(open("lr_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# Input widgets
year = st.slider("Model Year", 1995, 2025, 2015)
engine_size = st.number_input("Engine Size (L)", min_value=0.5, max_value=10.0, step=0.1)
cylinders = st.slider("Number of Cylinders", 2, 16, 4)
fuel_consumption = st.number_input("Fuel Consumption (L/100 km)", min_value=1.0, max_value=30.0, step=0.1)

# Prepare input
input_data = np.array([[year, engine_size, cylinders, fuel_consumption]])
input_scaled = scaler.transform(input_data)

# Predict button
if st.button("Predict CO2 Emissions"):
    prediction = model.predict(input_scaled)
    st.success(f"Estimated CO2 Emissions: {round(prediction[0], 2)} g/km")
