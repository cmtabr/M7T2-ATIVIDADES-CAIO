import streamlit as st 
from streamlit_extras.switch_page_button import switch_page
import requests
import json

st.title("Registry")

# Register form 
name = st.text_input("Name")
password = st.text_input("Password", type="password")
email = st.text_input("Email")
submit = st.button("Register")

obj = {
    "name": name,
    "password": password,
    "email": email
}

if obj["name"] == "":
    st.error("Name is required")
elif obj["password"] == "":
    st.error("Password is required")
elif obj["email"] == "":
    st.error("Email is required")

if submit and obj["name"] != "" and obj["password"] != "" and obj["email"] != "":
    print(obj)
    json_obj = json.dumps(obj)
    response = requests.post("http://localhost:8000/register", data=json_obj)
    if response.status_code == 201:
        st.success("Register successful")
        switch_page("Login")
    elif response.status_code == 409:
        st.error("User already exists")
    elif response.status_code == 500:
        st.error("Register failed")
    else:
        st.error("Internal server error")