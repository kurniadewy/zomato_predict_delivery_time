import streamlit as st
import pandas as pd
from utils import set_custom_theme

# Apply theme
set_custom_theme()

st.title("📈 Prediction History")

# Load from session state
history = st.session_state.get("history", [])

if not history:
    st.info("🔍 No prediction history found. Use the Single Prediction page to generate predictions.")
else:
    df = pd.DataFrame(history)
    df_expanded = pd.json_normalize(df.to_dict(orient='records'))

    # Optional: Rename for display
    df_expanded.rename(columns={'prediction': 'Predicted_Delivery_Time (minutes)'}, inplace=True)

    st.success(f"📦 Showing {len(df_expanded)} previous predictions.")
    st.dataframe(df_expanded)
