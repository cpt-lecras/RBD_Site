from mysql.connector import connect, Error

def db_connection():
    try:
        with connect(
                host="localhost",
                user="root",
                password="root",
                database="test",
        ) as connection:
            print(connection)
    except Error as e:
        print("ERROR"+e)