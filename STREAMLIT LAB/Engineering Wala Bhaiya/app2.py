import streamlit as st
st.title("Machine Learning Project")

# Import Images
from PIL import Image
img = Image.open("1.jpg")
st.image(img, width=300 , caption= "This is a Simple Image")

# Import Video
videofile = open("Musk.mp4", "rb")
play_video = videofile.read()
st.video(play_video)

# Import Audio
audiofile = open("pop.mp3", "rb").read()
st.audio(audiofile)

# Check Box
# ML Project : ( Select Gender M/F )
if st.checkbox("Show / Hide"):
    st.text("Show or Hide Widget")

# Radio Buttons
status = st.radio("What is your status?", ("Active", "Inactive"))

# Link with some functions
if status == "Active" :
    st.success("You are Active!")
else:
    st.warning("You are Inactive!")

# Select Box
occupation = st.selectbox("Select Your Occupation", ["Programmer", "Data Analyst", "Data Scientist" , "Doctor", "Businessman"])
st.write("You Selected the Option", occupation)

# Multiselect
location = st.multiselect("Where have you worked befor ?", ("Lucknow", "Gorakhpur", "Delhi", "Pune"))

# To get all selected count
st.write("You are selected !", len(location))

# Slider
level = st.slider("Select Your Level !", 1,10)

# To get all selected Level
st.write("You Level is !", level)

# Buttons
st.button("Simple Button One")
if st.button("Submit"):
    st.success("You have Submitted Sucessfully!")


st.button("Simple Button Two")
if st.button("Cancel"):
    st.warning("You have Canceled!")


## Text Input
firstName = st.text_input("Enter Your FullName " , "Type Here...")
if st.button("Submit",key= "1"):
    result = firstName.title()
    st.text("Your have Entered :")
    st.success(result)

# Text Area
message = st.text_area("Enter Your Message :", "Type Here...")
if st.button("Submit", key= "2"):
    result = message.title()
    st.text("You have written:")
    st.success(result)

# Date Input
import datetime
today = st.date_input("Today is :", datetime.datetime.now())
    
# Time
theTime = st.time_input("The Time is :", datetime.time())

# Display JSON Output
st.text("Display Json Data:")
st.json({
    "Name" : "Praveen Kumar Singh",
    "Gender" : "Male",
    "City" : "Lucknow",
    "Country" : "India"
})

# Display Raw Code : UseCase Blog
st.text("Display Raw Code : UseCase Blog")
st.code("""
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        import streamlit as st
        """)


# Display Raw Code with DataFrame
import streamlit as st

with st.echo():
    import pandas as pd
    df = pd.DataFrame(
        {
            "Name": ["Praveen Kumar Singh"],
            "Gender": ["Male"],
            "City": ["Lucknow"],
            "Country": ["India"]
        }
    )


# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting for 5 Seconds.."):
    time.sleep(5)
st.success("Finished!")
