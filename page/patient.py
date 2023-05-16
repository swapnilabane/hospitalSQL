import mysql.connector
import streamlit as st

def register_patient_detail(name, gender, age, address, contact):
    # Connect to the database and get the fines
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    patient_info = "insert into patient_detail (name, gender, age, address, contact) VALUES (%s, %s, %s, %s, %s)"
    data_patient = (name, gender, age, address, contact)
    cursor.execute(patient_info, data_patient)
    cnx.commit()
    cursor.close()
    cnx.close()

def get_patient_detail(name):
    #Get doctor details
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    get_info = "SELECT * FROM patient_detail WHERE name = %s"
    data_info = (name,)
    cursor.execute(get_info, data_info)

    # Convert list of tuples to list of dictionaries
    info = [{'patient_id': row[0], 'name': row[1], 'age': row[3], 'address': row[4], 'doctor_id': row[6], 'nurse_id': row[7]} for row in cursor.fetchall()]

    st.table(info)
    cursor.close()
    cnx.close()

    return info

def get_all_patient_detail():
    import pandas as pd
    #Get doctor details
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    get_info = "SELECT * FROM patient_detail"
    try:
        #data_info = (name, specialisation)
        cursor.execute(get_info)
        fetchall_obj = cursor.fetchall()
        if fetchall_obj:
            df = pd.DataFrame(columns=['Patient Id', 'name', 'age', 'Gender', 'address', 'contact', 'Doctor ID', 'Nurse ID'], data=fetchall_obj)
            st.table(df)
        else:
            st.error("Doctors database is empty")
    except:
        pass


    cnx.commit()
    cursor.close()
    cnx.close()


def del_patient_detail(name):
    #Delete doctor details
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    del_info = "DELETE FROM patient_detail WHERE name = %s"
    data_del = (name,)
    cursor.execute(del_info, data_del)
    cnx.commit()
    cursor.close()
    cnx.close()


def update_patient_detail(name, address, contact, patient_id):
    #Update patient details
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    update_info = "UPDATE patient_detail set name= %s, address= %s, contact= %s WHERE patient_id = %s"
    data_update = (name, address, contact, patient_id)
    cursor.execute(update_info, data_update)

    cursor.close()
    cnx.close()
