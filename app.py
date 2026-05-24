import streamlit as st
import pandas as pd
import joblib

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Waiter Tips Prediction",
    page_icon="🍽️",
    layout="centered"
)

# =====================================
# LOAD MODEL AND SCALER
# =====================================

model = joblib.load(
    "outputs/models/gradient_boosting.pkl"
)

scaler = joblib.load(
    "outputs/models/scaler.pkl"
)

# =====================================
# APP TITLE
# =====================================

st.title("🍽️ Waiter Tips Prediction App")

st.markdown(
    """
    Predict the expected waiter tip amount using Machine Learning.
    """
)

st.divider()

# =====================================
# USER INPUTS
# =====================================

total_bill = st.number_input(
    "💵 Total Bill Amount",
    min_value=1.0,
    max_value=1000.0,
    value=25.0,
    step=0.5
)

sex = st.selectbox(
    "👤 Gender",
    ["Female", "Male"]
)

smoker = st.selectbox(
    "🚬 Smoker",
    ["No", "Yes"]
)

day = st.selectbox(
    "📅 Day",
    ["Thur", "Fri", "Sat", "Sun"]
)

time = st.selectbox(
    "⏰ Meal Time",
    ["Lunch", "Dinner"]
)

size = st.slider(
    "👥 Number of People",
    min_value=1,
    max_value=10,
    value=2
)

st.divider()

# =====================================
# ENCODE INPUTS
# =====================================

sex_val = 0 if sex == "Female" else 1

smoker_val = 0 if smoker == "No" else 1

day_map = {
    "Fri": 0,
    "Sat": 1,
    "Sun": 2,
    "Thur": 3
}

day_val = day_map[day]

time_val = 0 if time == "Dinner" else 1

# =====================================
# PREDICTION
# =====================================

if st.button("🔮 Predict Tip"):

    # Create dataframe

    input_data = pd.DataFrame({

        'total_bill': [total_bill],
        'sex': [sex_val],
        'smoker': [smoker_val],
        'day': [day_val],
        'time': [time_val],
        'size': [size]

    })

    # Scale data

    input_scaled = scaler.transform(input_data)

    # Predict

    prediction = model.predict(input_scaled)

    predicted_tip = round(prediction[0], 2)

    # Show prediction

    st.success(
        f"💰 Predicted Tip Amount: ${predicted_tip}"
    )

    st.balloons()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📊 About Project")

st.sidebar.info(
    """
    This project predicts waiter tips using
    Machine Learning Regression Models.

    Best Model Used:
    Gradient Boosting Regressor
    """
)

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "Developed using Streamlit & Scikit-Learn"
)