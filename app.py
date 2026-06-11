import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('Model/house_price_prediction.pkl', 'rb'))

st.set_page_config(
    page_title="House Price Predictor",
    page_icon = "🏠"
)

st.title("House Price Predictor")

st.write("Enter property details to estimate the house price")

overall_qual = st.slider(
    "Overall Quanlity",
    1,
    10,
    5
)

gr_liv_area = st.number_input(
    "Ground Living Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=1500
)

garage_cars = st.number_input(
    "Garage Capacity (Cars)",
    min_value=0,
    max_value=5,
    value=2
)

garage_area = st.number_input(
    "Garage Area (sq ft)",
    min_value=0,
    max_value=1500,
    value=500
)

total_bsmt_sf = st.number_input(
    "Basement Area (sq ft)",
    min_value=0,
    max_value=5000,
    value=1000
)

year_built = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2025,
    value=2000
)

if st.button("Predict Price"):

    features = np.array([[
        overall_qual,
        gr_liv_area,
        garage_cars,
        garage_area,
        total_bsmt_sf,
        year_built
    ]])

    prediction = model.predict(features)

    usd_price = prediction[0]

    inr_price = usd_price * 90  # Approximate conversion

    st.success(
        f"Estimated House Price: $ {usd_price:,.2f}"
    )

    st.info(
        f"Approximate Price in INR: ₹ {inr_price:,.0f}"
    )