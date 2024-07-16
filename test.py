import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json 

st.set_page_config(page_title="Rupeek KPI View", page_icon=":bar_chart:", layout="wide")


st.title('Employee Home Location Tracker')

# Employee ID Input
employee_id = st.text_input('Enter your Employee ID', '')

employee_name = st.text_input('Enter your Name', '')

employee_local_address = st.text_input('Enter your current home location', '')

employee_pincode = st.text_input('Enter your home pincode', '')

city_list=['Bangalore','Pune','Chennai','Hyderabad','Delhi','Mumbai','Ahmedabad','Aurangabad','Bhopal','Chandigarh','Coimbatore','Faridabad','Ghaziabad','Guntur','Gurgaon','Hassan','Indore','Jaipur','Jodhpur','Kakinada','Karimnagar','Kolhapur','Kolkata','Lucknow','Ludhiana','Mysore','Nagpur','Nashik','Nizamabad','Noida','Pondicherry','Rajahmundry',
           'Rajkot','Shivmoga','Surat',
           'Tirupati','Vadodara','Vijayawada','Visakhapatnam','Warangal']
employee_city =  st.selectbox('Select your city', city_list, index=None )

if st.checkbox("Click here to locate my locattion"):
    loc = get_geolocation()
    latitude=loc.get('coords').get('latitude')
    longitude=loc.get('coords').get('longitude')


    st.map(latitude=latitude, longitude=longitude,)

