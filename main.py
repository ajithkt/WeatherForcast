import streamlit as st

st.title("Weather Frocast for the next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast days: ", min_value=1, max_value=5, help="Select the forcasted days")
option = st.selectbox("Select the data to view: ", ("Temperature", "Sky"))
st.title(f"{option} for the next {days} days in {place}")