
import streamlit as st
import pandas as pd
import numpy as np

# Set custom CSS for white background and black font
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: white !important;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Hello, World!")
st. header("Welcome to your first Streamlit app")
st.markdown("This is created by st.markdown")

col1, col2 = st.columns(2)

with col1:
    x = st.slider('Select an x value', 1, 10) 
with col2:
    st.write("the value of x is: ", x)

chart_data = pd.DataFrame(np.random.randn(20, 3),
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write(f"The value of x is: {x}")
# st.write("Welcome to your first Streamlit app