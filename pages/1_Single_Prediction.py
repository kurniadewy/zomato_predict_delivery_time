import streamlit as st
import joblib
import pandas as pd
from utils import set_custom_theme

# Apply custom theme
set_custom_theme()

# Page title
st.title("🔮 Single Delivery Prediction")
st.markdown("Fill in the order details below to estimate delivery time for a single order.")

# Load model and preprocessing tools
model = joblib.load('model_files/lgbm_model.pkl')
scaler = joblib.load('model_files/scaler.pkl')
label_encoders = joblib.load('model_files/label_encoders.pkl')
feature_columns = joblib.load('model_files/feature_columns.pkl')

# Section: Input
st.header("📝 Input Delivery Details")
input_data = {}

# Input columns
col1, col2 = st.columns(2)
with col1:
    input_data['City'] = st.selectbox("🌆 City", label_encoders['City'].classes_)
    input_data['Festival'] = st.selectbox("🎉 Festival Day", label_encoders['Festival'].classes_)
    input_data['Order_Day'] = st.selectbox("📆 Order Day", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    input_data['Road_traffic_density'] = st.selectbox("🚦 Traffic Density", label_encoders['Road_traffic_density'].classes_)
    input_data['Type_of_order'] = st.selectbox("🍽️ Order Type", label_encoders['Type_of_order'].classes_)
    input_data['multiple_deliveries'] = st.selectbox("📦 Multiple Deliveries", ['0', '1', '2', '3', '4'])

with col2:
    input_data['Type_of_vehicle'] = st.selectbox("🚚 Vehicle Type", label_encoders['Type_of_vehicle'].classes_)
    input_data['Vehicle_condition'] = st.slider("🛵 Vehicle Condition", 0, 2, 1)
    input_data['Weather_conditions'] = st.selectbox("🌤️ Weather Condition", label_encoders['Weather_conditions'].classes_)
    input_data['Time_Orderd'] = st.number_input("⏰ Time Ordered (e.g., 13.25)", 0.0, 24.0)
    input_data['Delivery_distance'] = st.number_input("📏 Delivery Distance (km)", 0.0, 100.0)

# Derive additional feature: Order_Hour
input_data['Order_Hour'] = int(input_data['Time_Orderd'])  # Ambil jam bulat

# Prediction Button
if st.button("🚀 Predict Delivery Time"):
    # Convert to DataFrame
    features = pd.DataFrame([input_data])

    # Apply label encoding
    for col, le in label_encoders.items():
        if col in features.columns:
            try:
                features[col] = le.transform(features[col])
            except Exception:
                st.error(f"❌ Invalid input for '{col}': {features[col].values[0]}")
                st.stop()

    # Filter only trained features
    features = features[[col for col in features.columns if col in feature_columns]]
    for col in feature_columns:
        if col not in features.columns:
            features[col] = 0
    features = features[feature_columns]

    # Scale and predict
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    prediction_minutes = round(prediction, 2)

    # Output
    st.header("📊 Prediction Result")
    st.metric("Estimated Delivery Time", f"{prediction_minutes} minutes")
