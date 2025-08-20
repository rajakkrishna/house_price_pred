import pandas as pd
import pickle as pk
import streamlit as st

with open(r'C:\Users\USER\OneDrive\Documents\House Price Pred\House_prediction_model.pkl', 'rb') as f:
    model = pk.load(f)


st.header('Bengaluru House Price Predictor')
data=pd.read_csv(r"C:\Users\USER\OneDrive\Documents\House Price Pred\bengaluru_house_prices.csv")

loc=st.selectbox("Choose the location",data['location'].unique())
sqft=st.number_input("Enter total sqft")
beds=st.number_input("Enter no. of bedrooms")
bath=st.number_input("Enter no. of bathrooms")
balc=st.number_input("Enter no. of balconies")

                
input = pd.DataFrame([[loc,sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony','bedrooms'])
if st.button('Predict Price'):
    try:
        prediction = model.predict(input)
        st.success(f"💰 Estimated Price: ₹ {prediction[0] * 100000:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")