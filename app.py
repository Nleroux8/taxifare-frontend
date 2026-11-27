import streamlit as st
import requests

"""
# Taxifare : How much is your taxi going to cost ?
"""

st.markdown(
    """
    ## Where are you trying to go ?

    ### Choose your location !
    """
)

from datetime import date
date_time = st.date_input("When do you want to leave ?", date.today(), date.today())

pickup_longitude = st.number_input('Insert your pickup longitude', -75.0, -73.0, -73.982123)

pickup_latitude = st.number_input('Insert your pickup latitude', 40.0, 41.0, 40.753404)

do_longitude = st.number_input('Insert your drop-off longitude', -75.0, -73.0, -73.980694)

do_latitude = st.number_input('Insert your drop-off latitude', 40.0, 41.0, 40.753947)

passenger_count = st.slider('Select passenger count', 1, 6, 2, 1)


api_url = st.secrets['API_URL']

params = {
    'pickup_datetime': date_time,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': do_longitude,
    'dropoff_latitude': do_latitude,
    'passenger_count': passenger_count
}
response = requests.get(api_url, params=params).json()

st.markdown(f"## Your taxi fare is ....... \n # {round(response['fare'], 2)} $$")
