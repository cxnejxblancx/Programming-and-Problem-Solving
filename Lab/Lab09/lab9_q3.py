def decode_roman_file(encoded_msg_file, decoded_msg_file):
    # try-except --> open file in read mode
    try:
        roman_file = open(encoded_msg_file)
    except FileNotFoundError:
        print(f"File at file pathway '{encoded_msg_file}' was not found.")
        return

    # variable
    roman_file_message = ""

    # for-loop --> read each line of the file
    for line in roman_file:
        roman_file_message += line.strip('\n')
        
    # variable
    secret_msg = decode_entire_msg(roman_file_message)

    # close file
    roman_file.close()

    # open new file in write mode
    secret_file = open(decoded_msg_file, 'w')

    # final print
    print(secret_msg, file = secret_file)

    # close file
    secret_file.close()

    # return
    secret_file

def decoded_part(message, start, end, step):
    # variable
    decoded = ""

    # for-loop
    for char in message[start: end: step]:
        decoded += char

    # return
    return decoded

def decode_entire_msg(message):
    # variables
    decoded_message = ""
    total_letters = 0

    start = 1
    index = 1
    step = int(message[0])

    # while-loop
    while total_letters < 100:
        # conditionals
        if message[index].isdigit():
            # variable
            decoded_word = decoded_part(message, start, index, step)

            # adjust variables
            decoded_message += decoded_word
            start = index + 1
            step = int(message[index])

        elif message[index].isalpha():
            total_letters += 1
        
        # adjust variable
        index += 1

    # return
    return decoded_message

def main():
    ROMAN_FILE = "roman_code_msg.txt"
    ROMAN_DECODED_FILE = "secret_msg.txt"
    decode_roman_file(ROMAN_FILE, ROMAN_DECODED_FILE)

main()
