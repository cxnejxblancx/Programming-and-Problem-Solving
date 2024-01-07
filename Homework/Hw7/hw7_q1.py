def get_word_count(file_pathway):
    # try / except
    try:
        # open file
        file_obj = open(file_pathway, 'r')
    
    except FileNotFoundError:
        # print
        print(f"WARNING: The file pathway '{file_pathway}' does not exist.")

        # return
        return 0
    
    # else is not necessary --> if 'FILENOTFOUNDERROR', since the except function returned a value, the code will not execute any code after that 

    # variables
    total_words = 0

    # sort through file
    for line in file_obj:

        # variable
        words_in_line = 0

        # for-loop
        for char in line:
            if (char == " ") or (char == "\n"):
                words_in_line += 1
        
        # adjust variable
        total_words += words_in_line

    # close file
    file_obj.close()

    # return
    return total_words
    

def main():
    # variable
    count = get_word_count("voltaire.txt")  # assumes txt file is in same directory
    
    # final print
    print(f"This file has {count} word(s).")

main()
