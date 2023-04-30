import mysql.connector
import streamlit as st


def log_user(loguname, logpassw):
    # Connect to the database
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    # Create a cursor object to execute SQL queries
    cursor = cnx.cursor()
    fetched_passw = "select password from user_data where username='" + loguname + "'"
    data_logs = (loguname,)
    cursor.execute(fetched_passw, data_logs)

    if logpassw == 1234:
        st.success("user authenticated", icon="🤖")
        row = fetched_passw.fetchall()
        for i in row:
            print(i, end="")
    else:
        st.error("Not authorized")


    st.table(logs_data)
    cursor.close()
    cnx.close()

    return logs_data


