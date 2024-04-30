import streamlit as st

# Import Image
from PIL import Image
img = Image.open("QUERY1.jpg")
st.image(img)

# Title
st.title("Machine Learning Project")

# Header
st.header("This is a Header")

# Subheader
st.subheader("This is a Subheader")

# Text
st.text("Hello Streamlit ! this is a Text")

# Markdown
st.markdown("# This is our First Markdown")

st.markdown("## This is our 2nd Markdown")

st.markdown("### This is our 3rd Markdown")

st.markdown("#### This is our 4th Markdown")

### Colorful Text

# Sucess 
st.success("Sucessful Done!!")

# Information
st.info("Information")

# Warning
st.warning("Warning Messase")

# Error
st.error("This is an Error")

# Exception
st.exception("Name Error ('Pandas is not defined')")

# Help

st.markdown("#### Pandas Help Using Streamlit!")
import pandas
st.help(pandas)

st.markdown("#### Python Help Range() Function Using Streamlit!")

st.help(range)


st.markdown("#### Streamlit Help  Using Streamlit!")

import streamlit
st.help(streamlit)

# Writing Text Super Function
st.write("Text With Write")

# Define Range
st.write(range(10))

