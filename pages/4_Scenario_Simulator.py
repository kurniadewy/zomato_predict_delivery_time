import streamlit as st
from utils import set_custom_theme

set_custom_theme()

st.title("⚙️ Scenario Simulator")

st.markdown("""
Enter your delivery conditions to get a recommendation for the **best vehicle type** and **optimal number of multiple deliveries**.
""")

col1, col2 = st.columns(2)
with col1:
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High", "Jam"], index=1)
    weather = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy", "Fog"], index=1)

with col2:
    distance = st.slider("Delivery Distance (km)", 0.0, 50.0, 5.0)

if st.button("Generate Recommendation"):
    # Logic
    if traffic in ["High", "Jam"] or weather in ["Rainy", "Fog"]:
        vehicle = "Motorcycle"
        multiple = 1
        insight = "Due to heavy traffic and/or poor weather, a motorcycle with single delivery is optimal for ensuring on-time delivery."
    
    elif distance > 20:
        vehicle = "Sedan"
        multiple = 0
        insight = "For long-distance delivery, it is recommended to avoid multiple deliveries to minimize delays. A sedan is suitable for longer trips."
    
    else:
        vehicle = "Scooter"
        multiple = 2
        insight = "Under good traffic and weather conditions with short distance, a scooter with multiple deliveries is efficient and cost-effective."

    # Output
    st.success(f"✅ Recommended Vehicle: **{vehicle}**")
    st.success(f"✅ Optimal Multiple Deliveries: **{multiple} packages**")
    
    # Insight
