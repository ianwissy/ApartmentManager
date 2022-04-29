import mysql.connector as db
from credentials import host, database, user, password


def connect_to_database():
    connection = db.connect(host=host, database=database, user=user, password=password)
    return connection


def get_table(name, connection):
    query = "select * from " + name
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()
