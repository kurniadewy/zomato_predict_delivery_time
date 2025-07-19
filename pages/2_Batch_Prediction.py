import streamlit as st
import pandas as pd
import joblib
from utils import set_custom_theme

# Apply custom theme
set_custom_theme()

st.title("📂 Batch Delivery Prediction")
st.markdown("Upload an Excel file containing multiple delivery records. Make sure your columns match the required format.")

# Load model and assets
model = joblib.load('model_files/lgbm_model.pkl')
scaler = joblib.load('model_files/scaler.pkl')
feature_columns = joblib.load("model_files/feature_columns.pkl")

# File uploader
file = st.file_uploader("📎 Upload Excel File", type=['xlsx'])

if file:
    try:
        df = pd.read_excel(file)

        # Tambahkan kolom yang hilang
        for col in feature_columns:
            if col not in df.columns:
                df[col] = 0

        # Susun ulang dan scale
        df = df[feature_columns]
        X_scaled = scaler.transform(df)

        # Prediksi
        predictions = model.predict(X_scaled)
        df['Predicted_Delivery_Time (minutes)'] = predictions

        # Display
        st.success(f"✅ {len(df)} records processed.")
        st.dataframe(df)

        # Download
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Result CSV", csv, file_name="predictions.csv")

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
