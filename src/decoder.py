import base64

def decode_keylogger_result(encoded_value, salt_length_in_bytes=8):
    # Ensure encoded_value is a valid integer string
    try:
        original_value = int(encoded_value) // 24  # Ensure `encoded_value` is numeric
    except ValueError as e:
        print(f"Error converting encoded value: {e}")
        return None, None

    # The rest of your decoding logic
    salt_length_in_bits = salt_length_in_bytes * 8
    key_binary = original_value >> salt_length_in_bits
    salt = original_value & ((1 << salt_length_in_bits) - 1)

    # Convert the binary data back to Base64 string
    key_base64_bytes = key_binary.to_bytes((key_binary.bit_length() + 7) // 8, 'big')
    key_base64 = key_base64_bytes.decode('utf-8')

    # Decode the Base64 string to the original key
    original_key_bytes = base64.b64decode(key_base64)
    original_key = original_key_bytes.decode('utf-8')

    return original_key, salt