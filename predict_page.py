import streamlit as st 
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data 
    
data = load_model()
xgmodel = data["model"]
encoder = data["le_encoder"]

def show_predict_page():
    st.title("Health insurance price prediction")
    st.write("""### We need some information to predict the Health insurance price """)

    gender = ("male","female")  
    smoking_status = ("yes","no")
    location = ("southeast","southwest","northwest","northeast")
    
    gender = st.selectbox("Select your gender", gender)
    age = st.slider("Select your age",18,60)
    children = st.slider("Number of children",0,10)
    location = st.selectbox("Select your location", location)
    bmi = st.number_input("Enter your Body Mass Index")
    smoking_status = st.selectbox("Do you smoke?", smoking_status)
    
    ok = st.button("Calculate the health insurance price")
    if ok:
        X = np.array([[age,gender,bmi,children,smoking_status,location]])
        X[:,1] = encoder.fit_transform(X[:,1])
        X[:,4] = encoder.fit_transform(X[:,4])
        X[:,5] = encoder.fit_transform(X[:,5])
        X = X.astype(float)
        pred_price = xgmodel.predict(X)
        st.subheader(f"The predicted health insurance price is ${pred_price[0]:.2f}")