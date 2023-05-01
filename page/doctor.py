import streamlit as st
import mysql.connector

def doctor_detail(name, specialisation, age, address, contact, fees, monthly_salary):
    # Connect to the database and get the fines
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    doctor_info = "insert into doctor_details (name, specialisation, age, address, contact, fees, monthly_salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data_doctor = (name, specialisation, age, address, contact, fees, monthly_salary)
    cursor.execute(doctor_info, data_doctor)
    cnx.commit()
    cursor.close()
    cnx.close()

def get_doctor_detail(name):
    #Get doctor details
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    get_info = "SELECT * FROM doctor_details WHERE name = %s"
    data_info = (name,)
    cursor.execute(get_info, data_info)

    # Convert list of tuples to list of dictionaries
    info = [{'name': row[0], 'specialisation': row[1], 'age': row[2], 'address': row[3]} for row in cursor.fetchall()]

    st.table(info)
    cursor.close()
    cnx.close()

    return info


def del_doctor_detail(name):
    #Delete doctor details
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    del_info = "DELETE FROM doctor_details WHERE name = %s"
    data_del = (name,)
    cursor.execute(del_info, data_del)
    cnx.commit()
    cursor.close()
    cnx.close()


def update_doctor_detail(name, specialisation, address, fees):
    #Update doctor details
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    update_info = "UPDATE doctor_details set specialisation= %s, address= %s, fees= %s WHERE name = %s"
    data_update = (specialisation, address, fees, name)
    cursor.execute(update_info, data_update)

    # updates = [{'name': row[0], 'specialisation': row[1], 'address': row[2], 'fees': row[3]} for row in cursor.fetchall()]
    #
    # st.table(updates)
    cursor.close()
    cnx.close()


