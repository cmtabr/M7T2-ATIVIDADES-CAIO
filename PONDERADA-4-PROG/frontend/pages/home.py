import streamlit as st 
import requests
import pandas as pd
import matplotlib as plt
import seaborn as sns

st.title("RDS Data Visualization")

# Define a function to fetch data from FastAPI
def get_data_from_api():
    response = requests.get(f"http://localhost:8000/embed-data")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Fetch data from FastAPI
data = get_data_from_api()

print(data)

columns = ['predictId', 'age', 'hypertension', 'heart_disease', 'work_type', 'avg_glucose_level', 'bmi', 'predicted', 'userId']

df = pd.DataFrame(data, columns=columns)
df = df.drop(columns=['userId', 'predictId'])
print(df)

st.dataframe(df)

age_predicted_counts = df.groupby(['age', 'predicted']).size().reset_index(name='count')

# Create side-by-side bar plots using Seaborn
fig = sns.catplot(data=df, x='age', hue='predicted', kind='count', height=6, aspect=2)
fig.set_axis_labels('Age', 'Count')
fig.fig.suptitle('Occurrence of Predicted by Age', y=1.02)
st.pyplot(fig)