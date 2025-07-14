{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4267a1bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "from sklearn.preprocessing import StandardScaler\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "92529b81",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-14 15:31:43.222 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:31:43.799 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\bhupe\\AppData\\Roaming\\Python\\Python312\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-07-14 15:31:43.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:31:43.801 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:31:43.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:31:43.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:31:43.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = pickle.load(open(\"lr_model.pkl\", \"rb\"))\n",
    "scaler = pickle.load(open(\"scaler.pkl\", \"rb\"))\n",
    "columns = pickle.load(open(\"columns.pkl\", \"rb\"))\n",
    "\n",
    "st.title(\"🚗 CO₂ Emission Predictor\")\n",
    "st.markdown(\"Predict how much CO₂ (in g/km) a bike/car will emit based on specifications.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "74980410",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-14 15:32:07.017 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.019 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.021 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.022 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.023 Session state does not function when running a script without `streamlit run`\n",
      "2025-07-14 15:32:07.026 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.027 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.027 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.029 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.029 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.030 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.030 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.032 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.033 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.033 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.034 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.035 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.036 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.037 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.037 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.037 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.038 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.038 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.040 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.040 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.041 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.042 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.042 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.043 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.044 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.044 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.045 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.045 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.046 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.046 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.046 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.047 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.047 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.048 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.048 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.048 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.049 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.054 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.054 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:07.055 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "year = st.number_input(\"Year\", min_value=1990, max_value=2030, value=2020)\n",
    "engine_size = st.number_input(\"Engine Size (L)\", min_value=0.5, max_value=10.0, value=2.0, step=0.1)\n",
    "cylinders = st.slider(\"Number of Cylinders\", 1, 16, 4)\n",
    "fuel = st.selectbox(\"Fuel Type\", ['Z', 'D', 'E', 'N', 'X'])\n",
    "transmission = st.selectbox(\"Transmission\", ['AS5', 'AS6', 'AV7', 'M5', 'A6'])  # Example options\n",
    "vehicle_class = st.selectbox(\"Vehicle Class\", ['SUV', 'COMPACT', 'MID-SIZE'])  # Example options\n",
    "make = st.selectbox(\"Manufacturer\", ['FORD', 'TOYOTA', 'HONDA'])  # Example options\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cf272457",
   "metadata": {},
   "outputs": [],
   "source": [
    "input_dict = {\n",
    "    'YEAR': year,\n",
    "    'ENGINE SIZE': engine_size,\n",
    "    'CYLINDERS': cylinders,\n",
    "    'FUEL_' + fuel: 1,\n",
    "    'TRANSMISSION_' + transmission: 1,\n",
    "    'VEHICLE CLASS_' + vehicle_class: 1,\n",
    "    'MAKE_' + make: 1\n",
    "}\n",
    "\n",
    "input_data = pd.DataFrame([input_dict])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0dc51236",
   "metadata": {},
   "outputs": [],
   "source": [
    "for col in columns:\n",
    "    if col not in input_data.columns:\n",
    "        input_data[col] = 0\n",
    "\n",
    "input_data = input_data[columns]  # Arrange in correct order\n",
    "input_scaled = scaler.transform(input_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9b4e7ffe",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-14 15:32:56.250 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:56.250 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:56.251 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:56.251 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:56.253 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-07-14 15:32:56.253 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button(\"Predict CO₂ Emission\"):\n",
    "    prediction = model.predict(input_scaled)[0]\n",
    "    st.success(f\"Estimated CO₂ Emission: **{prediction:.2f} g/km**\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
