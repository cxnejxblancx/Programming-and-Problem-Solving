def is_haiku(input_string):
    # variables
    qualified_haiku = False
    num_lines = input_string.count('/') + 1

    # conditional --> check if string has 3 lines
    if num_lines == 3:
        qualified_haiku = True

        # create list to split string into lines
        list_lines = input_string.split('/')
                
        # variables --> count number of syllables in each line
        first_syllables = list_lines[0].count(',') + 1
        second_syllables = list_lines[1].count(',') + 1
        third_syllables = list_lines[2].count(',') + 1

        # conditonals --> check if lines have correct number of syllables
        if ((first_syllables != 5) or (second_syllables != 7) or (third_syllables != 5)):
            qualified_haiku = False

            if first_syllables != 5:
                print("WARNING: The first line is not 5 syllables long.")
            
            if second_syllables != 7:
                print("WARNING: The second line is not 7 syllables long.")

            if third_syllables != 5:
                print("WARNING: The third line is not 5 syllables long.")
    else:
      print("WARNING: Incorrect number of lines.")
            
    # return
    return qualified_haiku


def haiku_string_parser(input_string):
    # conditionals
    if not is_haiku(input_string):
        return ""
    
    # separate haiku string by '/' into individual lines
    haiku_list = input_string.split('/')

    # variables
    redesigned_haiku = []

    # for-loop --> access each line in the haiku list
    for line in haiku_list:
        # variables
        new_line = []
        words_in_line = line.split(' ') # separate line by ' ' into individual words

        # for-loop --> access each individual word in the line list
        for ind_word in words_in_line:
            # adjust variables
            ind_word = ind_word.replace(',', '') # remove extra commas
            new_line.append(ind_word) # add the formatted words to the new_line list

        # adjust variable
        new_line = ' '.join(new_line) # convert line list to string
        redesigned_haiku.append(new_line) # add each line string to the formatted haiku list

    # adjust variable --> convert formatted haiku list into a string (each line printed on a new line)
    redesigned_haiku = '\n'.join(redesigned_haiku)

    # return
    return redesigned_haiku


def main():
    # variables
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)

    # final print
    print(formatted_haiku)

main()
