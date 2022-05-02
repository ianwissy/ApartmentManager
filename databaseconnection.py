import mysql.connector as db
from credentials import *


def connect_to_database():
    connection = db.connect(host=host,
                        database=database,
                        user=user,
                        password=password)
    return connection


def get_table(name):
    query = "select * from " + name
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def delete_row(table,id_name, id):
    connection = connect_to_database()
    query = "DELETE FROM " + table + " WHERE " + id_name + "='" + id + "'"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()



