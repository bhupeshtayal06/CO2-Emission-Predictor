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

## 📥 Input Parameters

The following parameters are used as input features in the CO₂ Emission Predictor app:

| Parameter                       | Description                                 | Example       |
|----------------------------------|---------------------------------------------|---------------|
| Engine Size (L)                 | Size of the vehicle's engine in liters      | 2.0           |
| Cylinders                       | Number of engine cylinders                  | 4             |
| Fuel Consumption City (L/100km)| Fuel used during city driving               | 9.5           |
| Fuel Consumption Hwy (L/100km) | Fuel used during highway driving            | 6.7           |
| Fuel Consumption Comb (L/100km)| Combined average fuel consumption           | 8.2           |
| Fuel Type                       | Type of fuel (e.g., Regular, Premium, Diesel)| Regular       |

---

## 📊 Dataset

This project uses a dataset containing various features related to vehicles like engine size, cylinders, fuel type, and fuel consumption to predict the CO₂ emissions of a vehicle.

- **Source:** [Canada Vehicle Fuel Consumption Ratings](https://www.kaggle.com/datasets/debajyotipodder/co2-emission-by-vehicles)

- **Dataset Files Used:**
  - `FuelConsumption.csv`
  - `emission.csv`

> 📁 These files are stored inside the `/datasets/` directory of the project.

---

## 🌐 Streamlit Web App

This project includes a user-friendly **Streamlit app** that allows users to predict CO₂ emissions of vehicles based on various input parameters.

### ⚙️ Streamlit App Features

- 🚗 Takes inputs like Engine Size, Number of Cylinders, Fuel Type, Transmission Type, and Fuel Consumption.
- 📉 Predicts the **CO₂ Emissions** using a trained Linear Regression model.
- 📊 Displays results instantly with a clean and interactive user interface.
- ✅ Validates inputs and performs preprocessing (e.g., scaling) before prediction.
- 📁 Model and scaler files are loaded from the `/saved_models/` directory.
- ☁️ Easily deployable on [Streamlit Community Cloud](https://streamlit.io/cloud).

> 💡 You can try the deployed app here: [CO2 Emission Predictor App](https://bhupeshtayal06-co2-emission-predictor-app-ott1xl.streamlit.app/)

---

## 🛠️ Technologies Used

This project utilizes the following technologies and tools:

- **Python** 🐍 – Programming language for data preprocessing, modeling, and building the Streamlit app.
- **Pandas** – For data analysis and manipulation.
- **NumPy** – For numerical computations.
- **Scikit-learn** – For building and evaluating machine learning models (Linear Regression, Random Forest, Decision Tree, SVR).
- **Matplotlib / Seaborn** – For visualization of trends and correlations (used in notebooks).
- **Streamlit** – For developing and deploying the interactive web application.
- **Pickle** – For model serialization and loading in the Streamlit app.
- **Git & GitHub** – Version control and code hosting.
- **Kaggle** – For accessing and utilizing the dataset.
- **Jupyter Notebooks** – For exploratory data analysis, model development, and visualization.
- **VSCode** – For coding and debugging.

---

## 🔄 Workflow

1. **Data Collection**
   - Downloaded the dataset from [Canada Government Open Data Portal](https://www.kaggle.com/datasets/debajyotipodder/co2-emission-by-vehicles).
   - Combined and cleaned multiple CSV files into a single dataset (`emission.csv`) for consistency.

2. **Data Preprocessing**
   - Selected important features: `ENGINE SIZE`, `CYLINDERS`, `FUEL CONSUMPTION`, `FUEL TYPE`, etc.
   - Handled categorical variables using label encoding or one-hot encoding as needed.
   - Applied `StandardScaler` for feature normalization.

3. **Model Building**
   - Trained multiple regression models:
     - **Linear Regression** ✅ (Best Performing)
     - Decision Tree Regressor
     - Random Forest Regressor
     - Support Vector Regressor (SVR)
   - Chose Linear Regression for final deployment based on performance.

4. **Model Evaluation**
   - Evaluated using metrics like:
     - R² Score
     - Mean Squared Error (MSE)
     - Root Mean Squared Error (RMSE)
   - Visualized predictions vs actual emissions for model assessment.

5. **Model Saving**
   - Used `pickle` to save:
     - Trained Linear Regression model (`lr_model.pkl`)
     - Scaler (`scaler.pkl`)
     - Column configuration (`columns.pkl`)

6. **Streamlit App Development**
   - Created a user interface to take inputs for engine size, cylinders, etc.
   - Display predicted CO₂ emission in grams/km.
   - Hosted the app on **Streamlit Community Cloud**.

7. **Deployment**
   - All project files pushed to [GitHub Repository](https://github.com/bhupeshtayal06/CO2-Emission-Predictor).
   - App deployed at: [CO2 Emission Predictor App](https://bhupeshtayal06-co2-emission-predictor-app-ott1xl.streamlit.app/)

---

## 📊 Evaluation Metrics

To evaluate the performance of different regression models, the following metrics were used:

| Metric | Description |
|--------|-------------|
| **R² Score (Coefficient of Determination)** | Measures how well the regression predictions approximate the real data points. Ranges from 0 to 1. Higher is better. |
| **Mean Absolute Error (MAE)** | The average of absolute differences between actual and predicted values. Lower is better. |
| **Mean Squared Error (MSE)** | The average of squared differences between actual and predicted values. Penalizes larger errors more than MAE. |
| **Root Mean Squared Error (RMSE)** | The square root of MSE. Interpretable in the same units as the target variable. Lower is better. |

### ✅ Best Performing Model: Linear Regression

| Metric | Value |
|--------|-------|
| **R² Score** | 0.9855 |
| **MAE**      | 6.71 g/km |
| **MSE**      | 76.05 |

---

## 📌 Results Snapshot

| Model                     | R² Score | MAE (g/km) | MSE       |
|--------------------------|----------|------------|-----------|
| **Linear Regression**   done  | 0.9855     | 6.71      | 76.05    |
| **Random Forest Regressor** done| 0.9692     | 5.54      | 161.26    |
| **Decision Tree Regressor** done | 0.9792     | 5.02      | 108.66    |
| **Support Vector Regressor (SVR)** done | 0.9019     | 10.52      | 513.74    |

---

## 🔮 Future Work

This project lays the foundation for CO₂ emissions prediction based on vehicle specifications. To further improve its performance and usability, the following enhancements can be made:

- 🚘 **Add More Parameters**: Incorporate additional features like weight, fuel tank capacity, tire type, and aerodynamics to enhance prediction accuracy.
- 📊 **More Models & Tuning**: Experiment with other advanced models like XGBoost, Gradient Boosting, and perform extensive hyperparameter tuning.
- 🌎 **Real-Time Prediction**: Integrate real-time APIs to predict emissions based on live vehicle data.
- 🌐 **Multi-Country Dataset**: Use datasets from various countries to make the model globally applicable.
- 🧠 **Deploy ML Model as API**: Convert the trained model into a REST API using Flask or FastAPI to make it usable across platforms.
- 📱 **Mobile-Friendly UI**: Improve UI/UX for better compatibility with mobile devices via Streamlit or Flutter integration.
- 📉 **Model Explainability**: Integrate SHAP or LIME libraries to explain model predictions to users.
- 🧪 **Automated Testing**: Add test cases for code robustness and continuous integration setup for production-ready deployment.

