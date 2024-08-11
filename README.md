Health Insurance Price Prediction
The project is also hosted on render platform you can check it out on: https://health-insurance-price-prediction-x472.onrender.com

Project Overview
This project aims to predict health insurance prices based on various factors such as age, gender, BMI, and other relevant features. 
The model developed can help insurance companies determine appropriate premiums for customers and provide insights into how different factors influence the pricing of health insurance.

Question 1: Why is this proposal important in today’s world? How predicting a health insurance cost accurately can affect the health care/insurance field?
Health care costs are rising nowadays hence prediction of health insurance costs could help many people. It can help an individual to choose the right and affordable insurance plan. Doctors can also plan treatment effectively and affordabily for patients. predicting health insurances can help companies plan further strategies and plans.

Question 2: If any, what is the gap in the knowledge, or how your proposed method can be helpful if required in the future for any other type of insurance?
There could be knowledge gaps due to various reasons like some sensitive datais restricted due to privacy. Also, there may be some missing values present that alters the accuracy of the models.
In medical domain, accuracy is of the highest important compared to others. Thus, health insurance trained models may not be used in other type of insurance since the risk factor and data is significantly different.

Objectives
Data Exploration & Preprocessing: Understand the dataset, clean it and perform exploratory data analysis (EDA) to discover patterns and relationships between variables.
Feature Engineering: Create and select meaningful features that have a significant impact on the insurance prices.
Model Development: Train various machine learning models to predict health insurance prices and evaluate their performance.
Model Evaluation & Optimization: Compare model performance using metrics like RMSE, MAE, and R-squared and fine-tune the best model for better accuracy.
Deployment: Provide code and web application that allows users to input their details and get an estimated insurance price.

Dataset
The dataset includes features such as:
Age: The age of the customer.
Gender: The gender of the customer.
BMI: Body Mass Index, a measure of body fat based on height and weight.
Children: The number of children covered by the insurance.
Smoker Status: Whether the customer is a smoker or not.
Location: The residential region of the customer.
Charges: The actual insurance charges (target variable).

Tools & Technologies
Programming Language: Python
Libraries:
Data Analysis: pandas, numpy
Data Visualization: matplotlib, seaborn
Machine Learning: scikit-learn
Modeling Techniques:
Linear Regression
Random Forest
XGBoost

Future Work
Explore deep learning models for potentially better performance.
Incorporate additional features such as medical history or lifestyle habits.
Extend the project to include different regions or demographic groups.

How to Run the Project
Clone the repository:
git clone https://github.com/yourusername/health-insurance-price-prediction.git
Install the required packages:
pip install -r requirements.txt
Run the Jupyter Notebook to train the model and make predictions:
jupyter notebook

The project is also hosted on render platform you can check it out on: https://health-insurance-price-prediction-x472.onrender.com
The saved_steps.pkl has the label encoder and the trained xgboost model.
You can use the streamlit run app.py command to run the app on local machine.


