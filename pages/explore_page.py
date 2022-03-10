import streamlit as st
import pandas as pd





def show_explore_page():

    st.title('Explore data')

    st.info('Upload the scrapped data here.')

    uploaded_file = st.file_uploader("Upload a file", type='csv')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)


    st.error('This Site Will Be Updated Soon ...')

    