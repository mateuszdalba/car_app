import streamlit as st
import pandas as pd
import pickle5 as pickle
from datetime import datetime


def show_predict_page():

    st.title('Predict car price based on provided information')
    
    st.info('All information must be provided in order to correctly predict the price.')

    unique_marks = list(pd.read_pickle('data/unique_marks.pkl')[0])

    df1 = pd.DataFrame(unique_marks).reset_index()
    df1['index'] = df1['index']+1

    true_false = (True, False)

    years = range(1950,2022)
    prod_year = st.number_input(label='Production year',value=2005, min_value=1950 , max_value=2023, step=1)

    parking_assist = st.radio(label='Does your car have parking assistant?',options=true_false, index=1)

    car_model = st.selectbox(label='Vehicle brand', options=unique_marks)

    horse_power = st.slider(label='Horse power [km]',min_value=30, value=120, step=1, max_value=500)

    automatic_gearbox = st.radio(label='Automatic transmission [gearbox]?',options=true_false, index=0)

    engine_capacity = st.number_input(label='Engine capacity [cm3]', value=1400, min_value=500, max_value=10000, step=1)

    car_mileage = st.slider(label='Car mileage [kilometers]',value=150000, min_value=1 , max_value=1000000, step=1)





    fuels = ('gasoline','gasoline+CNG','gasoline+LPG','diesel','hybrid')
    fuel = st.radio(label='Fuel',options=fuels, index=1)
    
    #Model
    loaded_model = pickle.load(open('models\model_cars.sav', 'rb'))

    button = st.button('Predict car price')

    if button:

        car_cat = df1.loc[df1[0] == car_model]['index']
        
        fuel_gasoline = 0
        fuel_gasoline_cng = 0
        fuel_gasoline_lpg = 0
        fuel_diesel = 0
        fuel_hybrid = 0

        if fuel == 'gasoline':
            fuel_gasoline+=1
        elif fuel== 'gasoline+CNG':
            fuel_gasoline_cng+=1
        elif fuel=='gasoline+LPG':
            fuel_gasoline_lpg+=1
        elif fuel=='diesel':
            fuel_diesel+=1
        elif fuel=='hybrid':
            fuel_hybrid+=1

        price = loaded_model.predict([[prod_year, parking_assist, car_cat, horse_power, automatic_gearbox,
                                    engine_capacity, car_mileage, fuel_gasoline,fuel_gasoline_cng,fuel_gasoline_lpg,fuel_diesel,fuel_hybrid]])

        st.success(f"""The price of this car should be around: ***{price[0]}*** PLN """)

    
        current_price = price[0]
        curr_price = pd.DataFrame({"pred":[current_price]})
        curr_price.to_pickle('data/latest_price.pkl')
        
        pred_time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        pred_t = pd.DataFrame({'time':[pred_time]})
        pred_t.to_pickle('data/pred_time.pkl')
    