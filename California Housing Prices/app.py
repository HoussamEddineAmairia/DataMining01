import streamlit as st
import numpy as np


st.title("House Price Prediction App")

st.write("Enter house details:")

longitude = st.number_input("Longitude", value=-122.0)
latitude = st.number_input("Latitude", value=37.0)
housing_median_age = st.number_input("Housing Median Age", value=20)
total_rooms = st.number_input("Total Rooms", value=2000)
total_bedrooms = st.number_input("Total Bedrooms", value=400)
population = st.number_input("Population", value=1000)
households = st.number_input("Households", value=300)
median_income = st.number_input("Median Income", value=3.0)

ocean = st.selectbox(
    "Ocean Proximity",
    ["INLAND", "NEAR OCEAN", "NEAR BAY", "<1H OCEAN", "ISLAND"]
)

if st.button("Predict Price"):

    input_data = np.array([[longitude, latitude, housing_median_age,
                            total_rooms, total_bedrooms, population,
                            households, median_income]])
    
    input_scaled = scaler.transform(input_data)

    log_price = model.predict(input_scaled)[0][0]

    price = np.expm1(log_price)

    st.success(f"🏠 Predicted Price: ${price:,.2f}")