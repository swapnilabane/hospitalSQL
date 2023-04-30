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