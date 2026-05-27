import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="Height Predictor App",
    page_icon="📏",
    layout="centered"
)

# 2. Application Title & Header
st.title("📏 Height Prediction System")
st.write("This web application uses a high-accuracy 2nd-degree Polynomial Regression model to estimate height based on weight data.")
st.markdown("---")

# 3. Load the Trained Pipeline Model Securely
@st.cache_resource
def load_model():
    # Using st.cache_resource keeps the model in memory so it runs instantly
    return joblib.load('perfect_height_predictor.joblib')

try:
    model = load_model()
    
    # 4. User Input Elements
    st.subheader("📊 Enter Individual Data")
    
    # Creates a visual slider for inputting weight values
    user_weight = st.slider(
        label="Select Weight (in kg):",
        min_value=20.0,
        max_value=150.0,
        value=60.0,
        step=0.5
    )
    
    # 5. Execution and Prediction Execution
    if st.button("Calculate Predicted Height", type="primary"):
        # Wrap input into a DataFrame matching the feature name from training
        input_df = pd.DataFrame({'Weight': [user_weight]})
        
        # Calculate the result
        predicted_height = model.predict(input_df)[0]
        
        # Display the result in a clean visual metric box
        st.success("Calculation Complete!")
        st.metric(
            label="Estimated Height", 
            value=f"{predicted_height:.2f} cm"
        )
        
        # Friendly contextual conversion for quick reference
        height_inches = predicted_height / 2.54
        feet = int(height_inches // 12)
        inches = int(height_inches % 12)
        st.info(f"Imperial conversion equivalent: **{feet} ft {inches} in**")

except FileNotFoundError:
    st.error("❌ Error: 'perfect_height_predictor.joblib' not found. Please run your model training script first to generate the file.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
