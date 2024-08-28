# decoder.py

import base64


def decode_keylogger_result(encoded_value):
    try:
        # Split the encoded value into the sentence and salt (if present)
        sentence_base64, salt_base64 = encoded_value.split(":")

        # Decode the Base64 string back to the original sentence
        sentence_bytes = base64.b64decode(sentence_base64)
        original_sentence = sentence_bytes.decode('utf-8')

        # Decode the salt for debugging or verification
        salt = base64.b64decode(salt_base64)
        return original_sentence, salt
    except ValueError:
        # Handle cases where there is no salt
        sentence_bytes = base64.b64decode(encoded_value)
        original_sentence = sentence_bytes.decode('utf-8')
        return original_sentence, None
