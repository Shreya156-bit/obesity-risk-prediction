
import streamlit as st
import pandas as pd
import joblib

# Load the trained machine learning model
saved_data = joblib.load("obesity_model.joblib")
model = saved_data["model"]

st.set_page_config(
    page_title="Obesity Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("Obesity Risk Prediction Using Machine Learning")
st.write(
    "Enter the details below to classify the obesity category "
    "based on the trained machine learning model."
)

st.info(
    "Educational project only. This model classifies categories "
    "learned from the dataset;"
    "It does not provide a medical diagnosis."
)

st.header("Enter Personal and Lifestyle Details")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age (years)", 14, 100, 25)
        height = st.number_input("Height (metres)", 1.20, 2.20, 1.65, 0.01)
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 65.0, 0.5)

        family_history = st.selectbox(
            "Family history of overweight?", ["yes", "no"]
        )
        favc = st.selectbox(
            "Frequent consumption of high-calorie food?", ["yes", "no"]
        )
        fcvc = st.selectbox(
            "Frequency of vegetable consumption (1–3)", [1.0, 2.0, 3.0]
        )
        ncp = st.selectbox(
            "Main meals per day", [1.0, 2.0, 3.0, 4.0]
        )
        caec = st.selectbox(
            "Eating between meals", ["no", "Sometimes", "Frequently", "Always"]
        )

    with col2:
        smoke = st.selectbox("Do you smoke?", ["yes", "no"])
        ch2o = st.selectbox(
            "Daily water consumption (1–3)", [1.0, 2.0, 3.0]
        )
        scc = st.selectbox(
            "Monitor calorie consumption?", ["yes", "no"]
        )
        faf = st.selectbox(
            "Physical activity frequency (0–3)", [0.0, 1.0, 2.0, 3.0]
        )
        tue = st.selectbox(
            "Technology use time (0–2)", [0.0, 1.0, 2.0]
        )
        calc = st.selectbox(
            "Alcohol consumption", ["no", "Sometimes", "Frequently", "Always"]
        )
        mtrans = st.selectbox(
            "Main mode of transportation",
            [
                "Public_Transportation",
                "Walking",
                "Automobile",
                "Motorbike",
                "Bike"
            ]
        )

    submitted = st.form_submit_button("Classify Category")

if submitted:
    input_data = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }])

    try:
        input_data = input_data[saved_data["feature_columns"]]
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted category: {prediction.replace('_', ' ')}")
    except Exception as error:
        st.error(f"Prediction error: {error}")
