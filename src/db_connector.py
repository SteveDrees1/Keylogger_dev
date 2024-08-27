import mysql.connector
from mysql.connector import Error
from config.db_config import DB_CONFIG

def connect_to_db():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error connecting to MySQL", e)
        return None
