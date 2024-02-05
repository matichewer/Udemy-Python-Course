import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider(
    "Forecast Days",
    min_value=1,
    max_value=5,
    value=1,
    help="Select the number of forecasted days",
)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Create a temperature plot
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            # Divido por 10 para obtener temperatura en C°, y redondeo a 2 decimales
            temperatures = [round(temp/10, 2) for temp in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(
                x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C°)"}
            )
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.error("Place not found")
