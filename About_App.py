import streamlit as st

st.image("logo_zomato.png", width=500)
st.markdown("<br>", unsafe_allow_html=True)
st.title("ℹ️ About This App")


st.markdown("""
Welcome to the **Zomato Delivery Time Estimator**, a web app designed to help estimate food delivery times based on order and delivery details.

---

### 🎯 Purpose of the App
This app aims to help:
- Estimate delivery duration before assigning a delivery partner
- Support decisions on routing and vehicle types
- Improve operational efficiency and customer satisfaction

---

### 🧭 How to Use This App

You can navigate through the sidebar:
- 🔍 **Single Prediction** – Fill in the delivery details to get one-time prediction
- 📁 **Batch Prediction** – Upload an Excel file with multiple orders
- ⏱ **Prediction History** – Review all previous predictions
- ⚙️ **Scenario Simulator** – Try different delivery setups

---

### 📝 Input Guidelines

When using the form, please fill in the following fields carefully:

| Field Name               | Description |
|--------------------------|-------------|
| `Order_Date`             | Date the order was placed (e.g., `2022-03-01`) |
| `Order_Hour`             | Hour of the order (0–23) |
| `Weather_conditions`     | Weather at the time of delivery (e.g., `Sunny`, `Stormy`) |
| `Road_traffic_density`   | Traffic level at that time (e.g., `Low`, `High`) |
| `Vehicle_condition`      | Condition of the delivery vehicle (scale: 0–5) |
| `Type_of_order`          | Type of food ordered (e.g., `Snack`, `Drinks`) |
| `Type_of_vehicle`        | Vehicle used (e.g., `motorcycle`, `scooter`) |
| `Multiple_deliveries`    | Number of deliveries done in the same trip |
| `Festival`               | Was it during a festival? (`Yes` / `No`) |
| `City`                   | Customer’s area type (`Metropolitan`, `Urban`, `Semi-Urban`) |
| `Distance_km`            | Estimated delivery distance in kilometers |

> ⚠️ Please make sure all inputs follow the correct format.

---

Built by **kurniadewy**
""")
