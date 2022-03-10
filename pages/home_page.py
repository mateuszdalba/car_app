import streamlit as st

def show_home_page():

    st.title('What is the main idea behind this app?')


    st.header('App functionalities')
    st.markdown("""\n
    1. Predict price of a car providing basic information
    2. Scrap data from otomoto.pl (~104 parameters avaliable)
    3. Explore the data and try to understand the car market in Poland
    4. Understand what influences the price of a car (ToDo)
    5. Automatically find profitable advertisments (e.g. where predicted price < real price) (ToDo)
    """)

    st.header('But why would I do this?')
    st.write("""
    There are couple of answers: 

    1. You want to know how much your car might be worth to e.g. sell it but you are not an expert. \n
    2. You might want to sell & buy cars for profit this tool might help you find profitable advertisments. (ToDo) \n
    3. You want to understand the car market to be even better expert. \n
    4. You want to explain the price of a car. (ToDo)
    """)

    st.header('Important Note')
    st.warning("""
    The data was scrapped from Polish site ***www.otomoto.pl*** therefore all insights,
    predictions etc. are only adequate to Polish car market. \n
    In the future, there might be an extension for other countries.
    """)

    

