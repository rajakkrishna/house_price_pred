# Bangalore House Price Prediction

A machine learning model to predict house prices in Bangalore using Linear Regression.

## Dataset
Uses `bengaluru_house_prices.csv` containing house data with features like location, size, total_sqft, bath, balcony, and price.

## Data Processing
- Cleaned location data by grouping locations with <10 entries as 'other'
- Extracted bedrooms count from size column
- Handled range values in total_sqft by taking averages
- Applied filters: sqft_per_bed >= 300 and price_per_sqft >= 2000

## Model
Linear Regression with OneHotEncoder for location and StandardScaler for numerical features.

## Output
- Trained model saved as `House_prediction_model.pkl`
- Cleaned dataset exported as `Cleaned_data.csv`
