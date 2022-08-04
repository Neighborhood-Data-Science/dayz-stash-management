"""
Main streamlit application backend implementation.
This will act as the main driver. Other helper streamlit implementations
will be called during build process.
"""

import addItems
import streamlit as st

PAGES = {
    "ServerName": addItems
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()