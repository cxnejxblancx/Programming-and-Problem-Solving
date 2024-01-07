def remove_Es(msg):
    """
    Removes all instances of E (upper and lowercase) from a str
        :param msg: str to have Es removed from
        :return: str of msg with Es removed
    """
    # variable
    new_msg = ""
  
    # for-loop --> get rid of and 'E's or 'e's in msg
    for char in msg:
        if (char != 'E') and (char != 'e'):
            new_msg += char
          
    # return 
    return new_msg

def remove_Es_new_file(filename):
    """
    Creates a new file where all instances of E (upper and lowercase) from
    filename are removed
        :param filename: str of file to be read
        :return: bool True if operation was successful, False if unsuccessful
    """
    # open file
    evil_e_file = open(filename, 'r')

    # open new file
    no_e_file = open("no_e_file.txt", 'w')

    # for-loop
    for line in evil_e_file:
        print(remove_Es(line), file = no_e_file)
    
    # close files
    evil_e_file.close()
    no_e_file.close()

    # return
    return no_e_file

def remove_Es_same_file(filename):
    """
    Updates filename file where all instances of E (upper and lowercase) are removed
        :param filename: str of file to be read
        :return: bool True if operation was successful, False if unsuccessful
    """
    # try-except --> open file in read mode
    try:
        evil_e_file = open(filename, 'r')
    except FileNotFoundError:
        print(f"File '{filename}' could not be found.")
        return False

    # open file in write mode
    new_e_file = open(filename, 'w')

    # for-loop
    for line in evil_e_file:
        line = remove_Es(line)
        print(line, file = new_e_file)
    
    # close files
    new_e_file.close()
  
    # return
    return True

def main():
    EVIL_ES_MSG = "evil_es_msg.txt"
    EVIL_ES_COPY = "evil_es_copy.txt" # a copy of the of message for testing purposes

    remove_Es_new_file(EVIL_ES_MSG)
    print(remove_Es_same_file(EVIL_ES_COPY))

main()
