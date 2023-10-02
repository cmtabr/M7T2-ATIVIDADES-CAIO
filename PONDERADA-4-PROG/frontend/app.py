import streamlit as st
import requests 
import json
from streamlit_extras.switch_page_button import switch_page
from extra_streamlit_components import CookieManager

cookie_manager = CookieManager()   

st.header('Login Section', divider='rainbow')

# Login form
name = st.text_input("Name")
password = st.text_input("Password", type="password")

col1,col2 = st.columns(spec=2, gap="small")
with col1:
    signup = st.button("Signup")
with col2:
    submit = st.button("Login")


obj = {
    "name": name,
    "password": password
}

if signup:
    switch_page("registry")

if submit:
    login_data = json.dumps(obj)
    print(login_data)
    try:
        response = requests.post("http://localhost:8000/login", data=login_data) 

        print(response.status_code)

        if response.status_code == 200:
            # Cookie successfully set
            st.success("Login successful. You can now access the authenticated content.")

            print(f'this is the reponse: {response.cookies}')
            token = response.cookies.get(list(response.cookies.keys())[0])
            token = token.split("'")
            token = token[3:4]
            cookie_manager.set("token", token[0]) 
            print(token)
            switch_page("home")           
        else:
            st.error("Login failed. Please check your credentials.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")