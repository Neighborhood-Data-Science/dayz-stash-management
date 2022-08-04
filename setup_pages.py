"""
Main streamlit application backend implementation.
This will act as the main driver. Other helper streamlit implementations
will be called during build process.
"""

import streamlit as st
import pandas as pd
import createNewStash
from streamlit_option_menu import option_menu


with st.sidebar:
    choose = option_menu("DayZ Stash Management", ["About", "View Stashes", "Add New Stash", "Share[?]"],
                         icons=['house', 'kanban', 'kanban','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "black"},
        "icon": {"color": "yellow", "font-size": "25px"},
        "nav-link-selected": {"background-color": "#02ab21"}
    }
    )

if choose == "About":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the App</p>', unsafe_allow_html=True)
        st.write('This is the about section. Stuff about the app will go here!')

elif choose == "Add New Stash":
    createNewStash.app()
