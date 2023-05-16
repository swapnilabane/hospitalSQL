import streamlit as st

import page.doctor
from page.doctor import doctor_detail, get_doctor_detail, del_doctor_detail, update_doctor_detail, get_all_doctor_detail
from page.adduser import user_data
from page.patient import register_patient_detail, get_patient_detail, get_all_patient_detail, del_patient_detail, update_patient_detail
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

from streamlit_card import card

import json
import requests
from streamlit_lottie import st_lottie

import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="This is a HM App")

with open('auth.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')



# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from doctor_details;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

def app():
    if authentication_status:
        st.title(f'Welcome to Hospital Management System')
        authenticator.logout('Logout', 'main')

        with st.sidebar:
            selected = option_menu(
                menu_title=None,
                options=['Home', 'Doctor', 'Patient', 'Nurse', 'About Us', 'Made By'],
                icons=['house', 'person', 'snow2', 'thermometer', 'snow', 'building', 'heart'],
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
            with st.sidebar:
                selected = option_menu(
                    menu_title=None,
                    options=['Register', 'Get Patient', 'Get All Patient', 'Delete Patient', 'Update Patient'],
                    icons=['person', 'snow2', 'snow', 'trash', 'card-list'],
                    menu_icon='cast',
                    default_index=0,
                    orientation="horizontal",
                    styles={
                        "container": {"padding": "0!important", "background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "15px"},
                        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px",
                                     "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "blue"},
                    }

                )

            if selected == 'Register':
                # Adding patients
                st.subheader("Register Patient Information")
                patient_name = st.text_input("Enter Patient Name", key="3")
                patient_gender = st.text_input("Enter Patient gender", key="4")
                patient_age = st.number_input("Enter Patient age", key="5")
                patient_address = st.text_input("Enter Patient address", key="6")
                patient_contact = st.text_input("Enter Patient contact", key="p_con")
                patient_btn = st.button("Submit", key='13')

                if patient_btn:
                    register_patient_detail(patient_name, patient_gender, patient_age, patient_address, patient_contact)
                    st.success("User added successfully.")

            if selected == 'Get Patient':
                st.subheader("Get Patient Details")
                patient_name = st.text_input("Enter Patient name", key="g_p_details")
                patient_btn = st.button("Submit")
                if patient_btn:
                    st.success("Details:")
                    get_patient_detail(patient_name)

            elif selected == 'Get All Patient':
                #st.subheader("Get All Doctor Details")
                st.write("Hello")
                patient_btn = st.button("Fetch all Patients", key='frm_fetch_all_doctors')
                if patient_btn:
                    get_all_patient_detail()

            elif selected == 'Delete Patient':
                st.subheader("Delete patient Details")
                patient_name = st.text_input("Enter patient name", key="788")
                patient_btn = st.button("Submit")
                if patient_btn:
                    del_patient_detail(patient_name)
                    st.success('Delete successfully')

            elif selected == 'Update Patient':
                st.subheader("Update patient Details")
                patient_id = st.number_input("Enter patient id", key="801")
                doc_name = st.text_input("Enter new patient name", key="790")
                doc_address = st.text_input("Enter New address", key="791")
                doc_contact = st.number_input("Enter New contact number", key="792", min_value=10, max_value=10)

                patient_btn = st.button("Update")
                if patient_btn:
                    update_patient_detail(patient_id, doc_name, doc_address, doc_contact)
                    st.success('Update successfully')

        elif selected == 'Doctor':

            with st.sidebar:
                selected = option_menu(
                    menu_title=None,
                    options=['Register', 'Get Doctor', 'Delete Doctor', 'Update Doctor'],
                    icons=['person', 'snow2', 'snow', 'trash', 'card-list'],
                    menu_icon='cast',
                    default_index=0,
                    orientation="horizontal",
                    styles={
                        "container": {"padding": "0!important", "background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "15px"},
                        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px",
                                     "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "blue"},
                    }

                )

            if selected == 'Register':
                # Adding patients
                st.subheader("Register Doctor Information")
                doctor_name = st.text_input("Doctor Name Insert", key="8")
                doctor_specialisation = st.text_input("Doctor Specialization Insert", key="9")
                doctor_age = st.number_input("Doctor age Insert", key="10")
                doctor_address = st.text_input("Doctor address Insert", key="11")
                doctor_contact = st.text_input("Doctor contact Insert", key="15")
                doctor_fees = st.number_input("Doctor fees Insert", key="99")
                doctor_monthly_salary = st.number_input("Doctor Monthly salary Insert", key="98")
                doctor_patient_id = st.number_input("Enter patient Id", key="998")
                doctor_btn = st.button("Submit", key='14')

                if doctor_btn:
                    doctor_detail(doctor_name, doctor_specialisation, doctor_age, doctor_address, doctor_contact, doctor_fees, doctor_monthly_salary, doctor_patient_id)
                    st.success("User added successfully.")

            elif selected == 'Get Doctor':
                st.subheader("Get Doctor Details")
                doctor_name = st.text_input("Enter doctor name", key="44")
                doctor_btn = st.button("Submit")
                if doctor_btn:
                    st.write("Details")
                    get_doctor_detail(doctor_name)

            elif selected == 'Get All Doctors':
                #st.subheader("Get All Doctor Details")
                doctor_btn = st.button("Show Doctors", key='frm_fetch_doctors')
                if doctor_btn:
                    get_all_doctor_detail()

            elif selected == 'Delete Doctor':
                st.subheader("Get all doctors details")
                doctor_btn = st.button("Show Doctors", key='frm_fetch_all_doctors')
                if doctor_btn:
                    get_all_doctor_detail()

                st.subheader("Delete Doctor Details")
                doctor_name = st.text_input("Enter doctor name", key="45")
                doctor_btn = st.button("Submit")
                if doctor_btn:
                    del_doctor_detail(doctor_name)
                    st.success('Delete successfully')

            elif selected == 'Update Doctor':
                st.subheader("Update Doctor Details")
                doc_name = st.text_input("Enter doctor name", key="49")
                doc_specialisation = st.text_input("Enter Doctor New Specialization", key="46")
                doc_address = st.text_input("Enter New address", key="47")
                doc_fees = st.number_input("Enter New fees", key="48")

                doctor_btn = st.button("Update")
                if doctor_btn:
                    update_doctor_detail(doc_name, doc_specialisation, doc_address, doc_fees)
                    st.success('Update successfully')

        elif selected == 'About Us':
            st.title('Vision')
            st.write('Vision To provide each patient with the world- class care, exceptional service and compassion we would want for our loved ones and To Lead the evolution of healthcare to enable every member of the communities we serve to enjoy a better, healthier life.')
            st.title('Mission')
            st.write('The mission of India Hospital is to provide quality health services and facilities for the community, to promote wellness, to relieve suffering, and to restore health as swiftly, safely, and humanely as it can be done, consistent with the best service we can give at the highest value for all concerned.')


        elif selected == 'Made By':
            st.title('Evaluation Nerds')
            # hasClicked = card(
            #     title="Hello World!",
            #     text="Surya",
            # )

    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
app()

