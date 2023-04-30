import mysql.connector

def patient_detail(name, sex, age, address, contact):
    # Connect to the database and get the fines
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    cursor = cnx.cursor()
    patient_info = "insert into patient_detail (name, sex, age, address, contact) VALUES (%s, %s, %s, %s, %s)"
    data_patient = (name, sex, age, address, contact)
    cursor.execute(patient_info, data_patient)
    cnx.commit()
    cursor.close()
    cnx.close()