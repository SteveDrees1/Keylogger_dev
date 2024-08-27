# decode_example.py

from decoder import decode_keylogger_result
from db_connector import connect_to_db
from mysql.connector import Error

def retrieve_and_decode_key(key_to_find):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Parameterized query to prevent SQL injection and ensure correct query syntax
            cursor.execute("SELECT key_pressed FROM keystrokes WHERE key_pressed = %s", (key_to_find,))

            # Fetch the result
            record = cursor.fetchone()

            if record:
                # Decode the retrieved encoded value
                original_key, salt = decode_keylogger_result(record[0])

                # Print the original key
                print(f"Decoded Key: {original_key}")
            else:
                print("No matching record found.")

        except Error as e:
            print("Failed to retrieve data from MySQL table", e)
        finally:
            cursor.close()
            connection.close()

