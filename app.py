import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

#Pages
from pages.predict_page import show_predict_page
from pages.explore_page import show_explore_page
from pages.home_page import show_home_page
from pages.scrap_page import show_scrap_page
from pages.profitable_page import show_profitable_page

#make it look nice from the start
st.set_page_config(page_title='Car app', page_icon="car")

st.sidebar.title("Navigation bar")
page = st.sidebar.radio('Go To:',
                ['Home',
                'Predict price',
                'Scrap data',
                'Find profitable ads',
                'Explore data'        
                 ])




# st.sidebar.title("About")
# st.sidebar.info(
#     """
#     The app is made for eductational purposes. \n
#     Latest update: 10.03.2022  \n
#     This app is maintained by Mateusz Dalba.  \n
#     Linkedin:
#     https://www.linkedin.com/in/mateusz-dalba-82184a115/.
#     """
#     )


if page == 'Predict price':

    st.sidebar.title("Technical information")
    st.sidebar.info(
    """
    ***Technique:*** Machine Learning \n
    ***Market:*** Polish cars \n
    ***Model:*** Random forest regressor \n
    ***Observations:*** ~23 000 \n
    ***Variables:*** 12 \n
    ***Train to test ratio:*** 70%/30% \n



    ***Quality metrics:*** \n
    ***R2:*** 95.86% \t
    ***MAE:*** 7753.66
    """
    )

    show_predict_page()
elif page == 'Explore data':

    st.sidebar.title("Tutorial")
    st.sidebar.info(
    """
    ToDo
    """
    )


    show_explore_page()
elif page == 'Scrap data':

    st.sidebar.title("Info")
    st.sidebar.info(
    """
    You can scrap data from available URLs. \n
    Just provide number of pages to be scrapped. \n
    The programm will gather information (~104 params) about cars automatically. \n
    After getting the data you can either download it or check EXPLORE PAGE. 
    """
    )


    show_scrap_page()
elif page == 'Home':

    st.sidebar.title("About")
    st.sidebar.info(
    """
    The app is made for eductational purposes. \n
    Latest update: 10.03.2022  \n
    This app is maintained by Mateusz Dalba.  \n
    Linkedin:
    https://www.linkedin.com/in/mateusz-dalba-82184a115/.
    """
    )


    show_home_page()

elif page == 'Find profitable ads':
    
    show_profitable_page()


latest_price = pd.read_pickle('data/latest_price.pkl')
pred_time = pd.read_pickle('data/pred_time.pkl')
st.sidebar.title("Latest activity")
st.sidebar.success(
    f"""
    ***Latest car price prediction:*** {latest_price.iloc[0][0]} PLN \n
    ***Latest prediction date:*** {pred_time.iloc[0][0]}
    """
    )


