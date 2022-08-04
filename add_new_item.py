"""
Main streamlit application backend implementation.
This will act as the main driver. Other helper streamlit implementations
will be called during build process.
"""

import addItems
import streamlit as st
from streamlit_option_menu import option_menu

PAGES = {
    "ServerName": addItems
}

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    page = PAGES[selected]
page.app()