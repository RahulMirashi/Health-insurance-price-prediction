import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict",{"Predict","Explore"})
st.sidebar.link_button("Get Code", "https://github.com/RahulMirashi/Health-insurance-price-prediction")
if page == "Predict":
    show_predict_page() 
else:
    show_explore_page()

