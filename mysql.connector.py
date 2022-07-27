import mysql.connector
from mysql.connector import Error


# Establishing connection

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             password=user_password)
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f"The error '{e}' occured")

    return connection


connection = create_connection('localhost', 'root', 'password')


def create_connection_db(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             password=user_password,
                                             database=db_name)
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f"The error '{e}' occured")

    return connection


connection1 = create_connection_db('localhost', 'root', 'password', 'library')


def execute_query(connection, query):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
