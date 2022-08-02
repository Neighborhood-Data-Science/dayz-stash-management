import streamlit as st
import pandas as pd
def app():
    
    movie_list = [
        "Matrix", "Blade Runner",
        "Forrest Gump","Avengers","Harry Potter"]

    option1 = st.selectbox('Select First Movie',movie_list)
    'You selected: ',option1
    option2 = st.selectbox('Select Second Movie',movie_list)
    'You selected: ',option2
    option3 = st.selectbox('Select Third Movie',movie_list)
    'You selected: ',option3

