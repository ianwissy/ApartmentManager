import mysql.connector as db
from credentials import *


def connect_to_database():
    connection = db.connect(host=host,
                        database=database,
                        user=user,
                        password=password)
    return connection


def get_query(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def send_query(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
