import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json 
import folium
from streamlit_folium import folium_static

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


if st.button("Click here to locate my locattion"):
    
        loc = get_geolocation()
        if loc is not None :
            print(type(loc))
            latitude=loc.get('coords').get('latitude')
            longitude=loc.get('coords').get('longitude')

            m = folium.Map(location=[latitude, longitude], zoom_start=15)
            folium.Marker([latitude, longitude], tooltip='You are here').add_to(m)

            with st.container():
                       folium_static(m,height= 400,width=400)
                       

            # st.map(latitude=latitude, longitude=longitude,)
        else :
              st.error('Click on Allow this Time to Capture Location')


