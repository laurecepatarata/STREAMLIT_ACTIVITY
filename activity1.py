import streamlit as st

# App title and intro
st.title("👋 Hello, Streamlit!")
st.header("🚀 Welcome to your first Streamlit app")
st.write("Use the inputs below and see how the app responds instantly!")

# Input fields
name = st.text_input("🧑 Enter your name:")
number = st.number_input("🔢 Enter your favorite number:", step=1)

# Conditional output
if name:
    st.success(f"Hello, {name}!")
    st.info(f"Your favorite number is: {number}")
else:
    st.warning("Please enter your name above.")