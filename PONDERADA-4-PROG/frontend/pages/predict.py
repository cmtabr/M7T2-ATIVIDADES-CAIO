import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
import requests
import json

st.title("Prediction")

# Predict form

binary_opt = ["Yes", "No"]
work_type_ans = ["Never Worked", "Children", "Governament Employee", "Private", "Self-employed"]


age = st.number_input("Age", min_value=0)
hypertension = st.selectbox("Hypertension", binary_opt)
heart_disease = st.selectbox("Heart Disease", binary_opt)
work_type = st.selectbox("Work Type", work_type_ans, )
avg_glucose_level = st.number_input("Average Glucose Level")
bmi = st.number_input("BMI")
submit = st.button("Predict")

from extra_streamlit_components import CookieManager

cookie_manager = CookieManager()   

token = cookie_manager.get("token")

obj = {
    "age": int(age),
    "hypertension": 0 if hypertension == "No" else 1,
    "heart_disease": 0 if heart_disease == "No" else 1,
    "work_type": work_type_ans.index(work_type),
    "avg_glucose_level": avg_glucose_level,
    "bmi": bmi,
    "token": token
}

print(obj)

if submit:
    print(obj)
    json_obj = json.dumps(obj)
    try:
        response = requests.post("http://localhost:8000/predict", data=json_obj)
        if response.status_code == 200:
            st.success("Prediction successful")
            switch_page("Home")
    except Exception as e:
        st.error("Something went wrong")
        print(e)