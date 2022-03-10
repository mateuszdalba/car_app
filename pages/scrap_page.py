import streamlit as st

try:
    from bs4 import BeautifulSoup
except :
    from BeautifulSoup import BeautifulSoup 


import requests
import pandas as pd

from functions.scrap import scrap_basic_info, make_line, scrap_full_info


def show_scrap_page():

    st.title('Scrap cars data from available sites')

    ava_urls = ('https://www.otomoto.pl/osobowe', 'dummyURL')
    urls = st.selectbox(label='Available URL', options=ava_urls)

    pages = st.slider(label='Number of pages to be fetched',value=1, min_value=1 , max_value=100, step=1)

    scrap_button = st.button('Start scrapping!')

    if scrap_button:

        df_basic = scrap_basic_info(url = urls, page=pages)
        st.success('Basic information scrapped, now scrapping details.')

        with st.spinner('Gathering data for you, please wait ...'):

            output = pd.DataFrame()
            for i in range(0,df_basic.shape[0]):
                #print(i)
                my_dict = scrap_full_info(i, basic_df=df_basic)
                output = output.append(my_dict, ignore_index=True)
            
            st.success('Done! Now you can download your data.')

        st.dataframe(output)

        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')
            
        csv = convert_df(output)
        st.download_button('Press to download',
        csv,
        'file.csv',
        "text/csv",
        key='download-csv'
        )