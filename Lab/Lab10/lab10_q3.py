def get_random_word(filepath):
    # import randint
    from random import randrange

    # open file
    file_obj = open(filepath, 'r')

    # variables
    words_in_file = []

    # for-loop
    for line in file_obj:
        words_in_line = line.split(' ')
        words_in_file += words_in_line
    
    # variables
    random_num = randrange(len(words_in_file))
    random_word = words_in_file[random_num]

    # return
    return random_word

def main():
    print(get_random_word("words.txt"))

if __name__ == '__main__':
    main()
    
