"""
Helper python file to populate the appropriate fields.
"""

import streamlit as st
import pandas as pd

def app():
    
    container_type = ['Crate', 'CargoTent','SeaChest','Barrell','Drybag Backpack']
    location_name = ['Cherno','Elektro','Tisy']

    select_container = st.selectbox('Select Container Type',container_type)
    'You selected: ',select_container
    select_location = st.selectbox('Select Location',location_name)
    'You selected: ',select_location

