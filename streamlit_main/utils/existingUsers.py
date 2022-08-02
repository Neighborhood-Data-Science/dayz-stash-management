import streamlit as st
import pandas as pd

def app():
    import streamlit as st
    from user_movie_mock_data import user_movie_mock_data

    output = []

    a_list = user_movie_mock_data.keys()

    st.title('Movie Recommender App')

    form = st.form(key='user-selector')
    form.markdown('Select a user from the list below')

    option = form.selectbox('', a_list)

    submit = form.form_submit_button('Submit')

    output = user_movie_mock_data.get(option)

    if submit and output:

        st.markdown("## Recommended Movies:")
        rec_list = "\n".join(output)
        st.markdown("```"+rec_list)