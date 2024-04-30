import streamlit as st
st.title("Happy Birthday Shivam!")

# Balloons
st.balloons()

# Sidebar
st.sidebar.header("About")
st.sidebar.text("This is our Demo Project.")

# Select Box
algorithms = st.sidebar.selectbox("Your Algorithm", ["Liner Regression", "Logistic Regression", "Decission tree", "Random Forest"])

