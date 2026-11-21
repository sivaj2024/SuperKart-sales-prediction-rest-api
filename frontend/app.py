import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"

# Set the title of the Streamlit app
st.title("Supermarket Sales Prediction")

# Section for online prediction
st.subheader("Online Prediction")

# Collect user input for property features
#room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
#accommodates = st.number_input("Accommodates (Number of guests)", min_value=1, value=2)
#bathrooms = st.number_input("Bathrooms", min_value=1, step=1, value=2)
#cancellation_policy = st.selectbox("Cancellation Policy (kind of cancellation policy)", ["strict", "flexible", "moderate"])
#cleaning_fee = st.selectbox("Cleaning Fee Charged?", ["True", "False"])
#instant_bookable = st.selectbox("Instantly Bookable?", ["False", "True"])
#review_scores_rating = st.number_input("Review Score Rating", min_value=0.0, max_value=100.0, step=1.0, value=90.0)
#bedrooms = st.number_input("Bedrooms", min_value=0, step=1, value=1)
#beds = st.number_input("Beds", min_value=0, step=1, value=1)

Product_Weight =  st.number_input("Product_Weight ", min_value=0, value=22)
Product_Sugar_Content = st.selectbox("Product_Sugar_Content?", ["Low Sugar", "Regular","No Sugar"])
Product_Allocated_Area = st.number_input("Product_Allocated_Area ", min_value=0.0, value=5.0)
Product_MRP = st.number_input("Product_MRP ", min_value=0, value=1000)
Store_Size =  st.selectbox("Store_Size", ["Small", "Medium","High"])
Store_Location_City_Type = st.selectbox("Store_Size", ["Tier 1", "Tier 2","Tier 3"])
Store_Type = st.selectbox("Store_Type", ["Supermarket Type1", "Supermarket Type2","Departmental Store","Food Mart"])
#Product_Id_char =  "FD",
Store_Age_Years = st.number_input("Store_Age_Years ", min_value=1, value=40)
Product_Type_Category = st.selectbox("Product_Type_Category", ["Non-Perishable", "Perishable"])

# Convert user input into a DataFrame
input_data = pd.DataFrame([{
    'Product_Weight': Product_Weight,
    'Product_Sugar_Content': Product_Sugar_Content,
    'Product_Allocated_Area': Product_Allocated_Area,
    'Store_Size': Store_Size,
    'Product_MRP': Product_MRP,
    'Store_Location_City_Type': Store_Location_City_Type,
    'Store_Type': Store_Type,
    'Store_Age_Years': Store_Age_Years,
    'Product_Type_Category': Product_Type_Category
}])

# Make prediction when the "Predict" button is clicked
if st.button("Predict", type="primary"):
    response = requests.post(f"{BACKEND_URL}/v1/SuperKart", json=input_data.to_dict(orient='records')[0])  # Send data to Flask API
    if response.status_code == 200:
        prediction = response.json()['Predicted Sales (in dollars)']
        st.success(f"Predicted Sales  (in dollars): {prediction}")
    else:
        st.error("Unable to connect to the prediction API.")

# Section for batch prediction
st.subheader("Batch Prediction")

# Allow users to upload a CSV file for batch prediction
uploaded_file = st.file_uploader("Upload CSV file for batch prediction", type=["csv"])

# Make batch prediction when the "Predict Batch" button is clicked
if uploaded_file is not None:
    if st.button("Predict Batch", type="primary"):
        response = requests.post(f"{BACKEND_URL}/v1/SuperKartBatch", files={"file": uploaded_file})  # Send file to Flask API
        if response.status_code == 200:
            predictions = response.json()
            st.success("Batch predictions completed!")
            st.write(predictions)  # Display the predictions
        else:
            st.error("Unable to connect to the prediction API.")
