import mysql.connector

def user_data(username, password):
    # Connect to the database
    cnx = mysql.connector.connect(
        user="root",
        password="swap",
        host="localhost",
        database="newdb"
    )

    # Create a cursor object to execute SQL queries
    cursor = cnx.cursor()
    add_info = "INSERT INTO user_data (username, password) VALUES (%s, %s)"
    data_info = (username, password)
    cursor.execute(add_info, data_info)
    cnx.commit()
    cursor.close()
    cnx.close()
