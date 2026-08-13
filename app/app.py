#  Crop Recommendation Web App
# --------------------------------------------------
# Run using: streamlit run app.py
# --------------------------------------------------

import streamlit as st
import pandas as pd
import joblib

# Load trained model and preprocessing objects
model = joblib.load('../models/crop_model.pkl')
scaler = joblib.load('../models/scaler.pkl')
label_encoder = joblib.load('../models/label_encoder.pkl')

#  App title and description
st.set_page_config(page_title="Crop Recommendation Systemssssssss", page_icon="🌾", layout="centered")

st.title("Crop Recommendation System")
st.markdown("""
This system predicts the **most suitable crop** for cultivation based on soil and weather conditions.
Provide your field parameters below 👇
""")

#  Input fields for parameters
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=90)
    P = st.number_input("Phosphorous (P)", min_value=0, max_value=200, value=42)
    K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=43)
    ph = st.number_input("pH value", min_value=0.0, max_value=14.0, value=6.5)

with col2:
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.5)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=80.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0)

# Prediction button
if st.button(" Recommend Crop"):
    # Prepare input data
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    
    # Scale input data
    input_scaled = scaler.transform(input_data)

    # Predict crop
    prediction = model.predict(input_scaled)
    crop_name = label_encoder.inverse_transform(prediction)[0]
    
    # Display result
    st.success(f"Recommended Crop: **{crop_name}**")
    st.balloons()

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit | Crop Recommendation ML Model")
