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
    message = "3Gn.olwo pd/Q gh5l!d pulAk c_kosk an2 moPn! .y\oausr? 3mqei,sd+ktcbe.KrkcmOpsne!se odYpqo>kulq fag pozrtks dftpqh /ipaslk!dp4vm fkofwolp9 mjcnre"
    
    print(decode_entire_msg(message))

main()
