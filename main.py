import streamlit as st
import plotly.express as px
from backend import getdata

st.title("Weather Forecast for the next Days")
place = st.text_input("Place: ")
days = st.slider("Forcast days: ", min_value=1, max_value=5, help="Select the forcasted days")
option = st.selectbox("Select the data to view: ", ("Temperature", "Sky"))
st.title(f"{option} for the next {days} days in {place}")


if place:
    filtered_data = getdata(place, days )
    if option == "Temperature":
        temperature_data = [i["main"]["temp"] for i in filtered_data]
        dates = [i['dt_txt'] for i in filtered_data]
        figure = px.line(x=dates, y=temperature_data, labels={"x": "dates", "y": "temperature"})
        st.plotly_chart(figure)
    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_data = [i["weather"][0]['main'] for i in filtered_data]
        images_data = [images[i] for i in sky_data]
        st.image(images_data, width=115)


