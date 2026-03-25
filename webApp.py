import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('linear_model.pkl', 'rb')) 
carData = pd.read_csv('data.csv')

st.title("Car Price Predictor 🚗")

year = st.number_input("Year", min_value=2000, step=1)
distance = st.number_input("Distance covered (kms)", min_value=0)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG"])

companyName = st.selectbox(
    "Company Name", 
    sorted(carData['company'].unique())
)

if companyName:
    modelOptions = carData[carData["company"] == companyName]["name"].unique()

    modelOptions = [name.replace(companyName, "").strip() for name in modelOptions]

    modelName = st.selectbox("Model Name", sorted(modelOptions))

    if st.button("Predict Price"):
        input_df = pd.DataFrame([{
            "year": year,
            "kms_driven": distance,
            "fuel_type": fuel_type,
            "model": modelName,   
            "company": companyName
        }])

        prediction = model.predict(input_df)[0]

        st.success(f"Estimated Price: ₹ {round(prediction, 2)}")