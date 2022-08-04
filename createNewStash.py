"""
Helper python file to populate the appropriate fields.
"""

import streamlit as st
import pandas as pd

def app():

    with st.form('Create New Stash'):
        container_type = ['','Crate', 'CargoTent','SeaChest','Barrell','Drybag Backpack']
        location_name = ['','Cherno','Elektro','Tisy']
        category_name = ['','Food and Drink','Ammunition','Magazines','Medical']
        item_name = ['','Apple','FX-45','Bandage']

        st.text_input('Title',placeholder="Enter a new title for your stash.")
        #Select container type
        select_container = st.selectbox('Stash Type',container_type)
        #Select location name
        select_location = st.selectbox('Location',location_name)
        #Select category of item
        select_category = st.selectbox('Category',category_name)
        #Select item based on category (if checked) otherwise, return all items
        select_item = st.selectbox('Item',item_name)
        #Enter the number of items to add
        enter_quantity = st.number_input('Enter quantity', min_value=0)

        #Add submit button
        add_item_button = st.form_submit_button("Add Item")
        if add_item_button:
            st.write("Updated!")


    ###
    ### Item image should pop up once item name is selected
    ### If an option is blank, do not let the user make a submission (except for Category)

    



