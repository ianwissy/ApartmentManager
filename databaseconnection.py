import mysql.connector as db

def connect_to_database():
    connection = db.connect(host='classmysql.engr.oregonstate.edu',
                        database="cs340_wysei",
                        user="cs340_wysei",
                        password="6820")
    return connection

def get_table(name, connection):
    query = "select * from " + name
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()
