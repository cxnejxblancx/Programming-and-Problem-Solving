def get_last_char(filename):
    """
    Grabs the last alphabetic character of a pre-existing file with content
        :param filename: name of the file to grab the last character from
        :return: char present at the end of the character or None otherwise
    """
    # try-except --> open file in read mode
    try:
       alpha_file = open(filename, 'r')
    except FileNotFoundError:
       return None

    # variables
    existing_chars = ""

    # for-loop
    for line in alpha_file:
        line = line.strip()
        existing_chars += line

    # conditonals
    if len(existing_chars) == 0:
        return None
    else:
        return existing_chars[-1]

def alphabet_soup(filename):
    """
    Creates or continues an alphabet in file `alphabet.txt`.
        :param filename: name of the file to create or continue the alphabet in
    """
    # open file in append mode
    alpha_file = open(filename, 'w')

    # variable
    alpha_str = "abcdefghijklmnopqrstuvxyz"
        
    # conditonals --> check if file completely empty or unfinished
    if get_last_char(filename) == None:
        # for-loop
        for char in alpha_str:
            print(char, file = alpha_file)

    else:
        # variables
        last_char = get_last_char(filename)
        last_index = alpha_str.find(last_char)

        # for-loop
        for char in alpha_str[(last_index + 1):]:
            print(char, file = alpha_file)

    # return
    return alpha_file
            
def main():
    ALPHABET_FILE = "alphabet.txt"
    alphabet_soup(ALPHABET_FILE)

main()
