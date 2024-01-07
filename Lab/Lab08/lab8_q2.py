# decode a single letter
def decode_letter(char, key):
    a_upper_ascii = 65
    z_upper_ascii = 90

    a_lower_ascii = 97
    z_lower_ascii = 122

    if char.isupper():
        if (ord(char) - key) < a_upper_ascii:
            decoded_char = chr(z_lower_ascii - ((a_upper_ascii - (ord(char) - key)) + 1))
        else: 
            decoded_char = chr(ord(char) - key)
    
    else:
        if (ord(char) - key) < a_lower_ascii:
            decoded_char = chr(z_lower_ascii - ((a_lower_ascii - (ord(char) - key)) + 1))
        else: 
            decoded_char = chr(ord(char) - key)

    return decoded_char

# accept encoded_message and decode it
def decode_caesar(encoded_message, key):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            decode_letter(char, key)
            decoded_message += decode_letter(char, key)
        else:
            decoded_message += char

    return decoded_message

# decode single word
def main():
    """
    Just some sample behavior.
    """
    decryption_key = 3
    line = input("Enter the encoded line: ")
    decryption = decode_caesar(line,decryption_key)
    print(decryption)

main()
