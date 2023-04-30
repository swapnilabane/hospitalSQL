import streamlit as st
from page.doctor import doctor_detail
from page.adduser import user_data
from page.patient import patient_detail
from streamlit_option_menu import  option_menu
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="This is a HM App")

def app():

    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=['Home', 'Register', 'Doctor', 'Patient', 'About Us', 'Made By'],
            icons=['house', 'person', 'snow2', 'thermometer', 'building', 'heart'],
            menu_icon='cast',
            default_index=0,

        )

    if selected == 'Home':
        url = requests.get(
            "https://assets10.lottiefiles.com/packages/lf20_mR5H7A.json")
        # Creating a blank dictionary to store JSON file,
        # as their structure is similar to Python Dictionary
        url_json = dict()

        if url.status_code == 200:
            url_json = url.json()
        else:
            print("Error in the URL")

        st.title("Hospital Management")

        st_lottie(url_json,
                  # change the direction of our animation
                  reverse=True,
                  # height and width of animation
                  height=600,
                  width=800,
                  # speed of animation
                  speed=0.8,
                  # means the animation will run forever like a gif, and not as a still image
                  loop=True,
                  # quality of elements used in the animation, other values are "low" and "medium"
                  quality='high',
                  # THis is just to uniquely identify the animation
                  key='Car'
                  )

    elif selected == 'Register':

        # Create a form to insert a user
        st.subheader("Register User")
        main_user = st.text_input("Username Insert", key="1")
        main_pass = st.text_input("Enter password", key="2")

        if st.button("Submit", key='12'):
            user_data(main_user, main_pass)
            st.success("User added successfully.")

    elif selected == 'Patient':
        # Adding patients
        st.subheader("Register Patient Information")
        patient_name = st.text_input("Patient Name Insert", key="3")
        patient_sex = st.text_input("Patient sex Insert", key="4")
        patient_age = st.number_input("Patient age Insert", key="5")
        patient_address = st.text_input("Patient address Insert", key="6")
        patient_contact = st.text_input("Patient contact Insert", key="7")
        patient_btn = st.button("Submit", key='13')

        if patient_btn:
            patient_detail(patient_name, patient_sex, patient_age, patient_address, patient_contact)
            st.success("User added successfully.")

    elif selected == 'Doctor':
        # Adding patients
        st.subheader("Register Doctor Information")
        doctor_name = st.text_input("Doctor Name Insert", key="8")
        doctor_specialisation = st.text_input("Doctor Specialization Insert", key="9")
        doctor_age = st.number_input("Doctor age Insert", key="10")
        doctor_address = st.text_input("Doctor address Insert", key="11")
        doctor_contact = st.text_input("Doctor contact Insert", key="15")
        doctor_fees = st.number_input("Doctor fees Insert", key="99")
        doctor_monthly_salary = st.number_input("Doctor Monthly salary Insert", key="98")
        doctor_btn = st.button("Submit", key='14')

        if doctor_btn:
            doctor_detail(doctor_name, doctor_specialisation, doctor_age, doctor_address, doctor_contact, doctor_fees, doctor_monthly_salary)
            st.success("User added successfully.")

    elif selected == 'About Us':
        st.title('About us')

    elif selected == 'Made By':
        st.title('Made By')
app()

