"""
Helper python file to populate the appropriate fields.
"""

import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

@st.cache
def get_image_data():
    path = r'dayz_images_info.csv'
    return pd.read_csv(path)

@st.cache
def get_city_names():
    path = r'chernarus_cities.csv'
    return pd.read_csv(path)

image_info = get_image_data()
city_names = get_city_names()


def update_item_list():
    """
    Update item list based on category selection
    """
    item_list = image_info[image_info['Category']==st.session_state.item_Category].loc[:,'item_Name'].tolist()

def update_image():
    """
    Update the image based on item selection.
    """
    image_link = image_info[image_info['item_Name']==st.session_state.item_Name].loc[:,'image_Link'].tolist()[0]
    image_request = requests.get(image_link)
    image = Image.open(BytesIO(image_request.content))

def app():
    #Set variables (for now)
    container_type = ['','Crate', 'CargoTent','SeaChest','Barrell','Drybag Backpack']
    
    st.text_input('Title',placeholder="Enter a new title for your stash.")

    #Select container type
    select_container = st.selectbox('Stash Type',container_type, key='container_Name')

    #Select location name
    location_name = city_names.loc[:,'Location'].tolist()
    select_location = st.selectbox('Location',location_name,key='location_Name')

    #Select category of item
    category_name = image_info.loc[:,'Category'].unique().tolist()
    select_category = st.selectbox('Category',category_name,key='item_Category',on_change=update_item_list)

    #Select item based on category (if checked) otherwise, return all items
    if select_category:
        item_list = image_info[image_info['Category']==select_category].loc[:,'item_Name'].tolist()
        select_item = st.selectbox('Item',item_list,key='item_Name', on_change = update_image)
    

    #Insert image of item once name is selected
    if item_list:
        image_link = image_info[image_info['item_Name']==select_item].loc[:,'image_Link'].tolist()[0]
        image_request = requests.get(image_link)
        image = Image.open(BytesIO(image_request.content))
        st.image(image, caption='Selected Item')   

    #Enter the number of items to add
    enter_quantity = st.number_input('Enter quantity', min_value=0)

    #Add submit button
    add_item_button = st.button("Add Item")
    if add_item_button:
        st.write("Updated!")


    ###
    ### Item image should pop up once item name is selected
    ### If an option is blank, do not let the user make a submission (except for Category)

    



