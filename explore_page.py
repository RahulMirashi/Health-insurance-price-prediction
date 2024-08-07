import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_excel("Health_insurance_cost.xlsx")

    df = df.dropna(subset=['age'])
    df = df.dropna(subset=['BMI'])
    df = df.dropna(subset=['health_insurance_price'])
    return df

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data 

df = load_data()
data = load_model()
xgmodel = data["model"]
encoder = data["le_encoder"]

def show_explore_page():
    st.title("Explore Health Insurance prices")
    st.subheader("Following is the health insurance Dataset used")
    st.dataframe(df)

    # Scatter plot
    fig, ax = plt.subplots()
    colors = {'male': 'blue', 'female': 'pink'}
    x=df['age']
    y=df['health_insurance_price']
    ax.scatter(x, y, c=df['gender'].map(colors))
    ax.set_title('Age vs. Health Insurance Price')
    ax.set_xlabel('Age')
    ax.set_ylabel('Health insurance price')
    st.pyplot(fig)
    st.write("""After analyzing the scatter plot for age vs health insurance prices value we can infer that majority of 
    the concentration lies in the 0 to 15000 price range for all the age groups and it gradually reduces as the prices increases.
    Also we can conclude that as the age group value increases from 0 to 70 the average health insurance prices are also increasing.""")
    
    # Bar plot
    fig, ax = plt.subplots()
    sns.barplot(x=df['location'], y=df['health_insurance_price'], data=df, ax=ax, palette='viridis')
    ax.set_title('Health insurance price as per location')
    ax.set_xlabel('Location')
    ax.set_ylabel('Health insurance price')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.barplot(x=df['gender'], y=df['health_insurance_price'], data=df, ax=ax, palette='viridis')
    ax.set_title('Health insurance price as per Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Health insurance price')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.barplot(x=df['smoking_status'], y=df['health_insurance_price'], data=df, ax=ax, palette='viridis')
    ax.set_title('Health insurance price as per Gender')
    ax.set_xlabel('Smoking status')
    ax.set_ylabel('Health insurance price')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    colors = {'male': 'blue', 'female': 'pink'}
    x=df['BMI']
    y=df['health_insurance_price']
    c=df['smoking_status']
    ax.scatter(x, y, c=df['gender'].map(colors))
    ax.set_title('Relationship between BMI and Charges')
    ax.set_xlabel('BMI')
    ax.set_ylabel('Health insurance price')
    st.pyplot(fig)

    df['gender'] = encoder.fit_transform(df['gender'])
    df['smoking_status'] = encoder.fit_transform(df['smoking_status'])
    df['location'] = encoder.fit_transform(df['location'])
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True).round(2), ax=ax, annot=True)
    ax.set_title('Correlation Heatmap')
    st.write(fig)  
    st.write("""From the heatmaps for correlation between the variables we can clearly infer that the value of health insurance price 
    is majorly dependent on whether the person is smoker or not and from the above scatterplot as well we can predict that 
    on average person who smokes as a higher value of health insurance than a non-smoking person. We can also see that health 
    insurance price is also dependent on the age of the person. Health insurance price is direct proportional to age""")
    
