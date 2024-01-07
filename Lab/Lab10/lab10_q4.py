def shuffle_create(old_list):
    # import randrange
    from random import randrange

    # variables
    shuffled_list = []
    random_num_list = []
    # for-loop
    for index in range(len(old_list)):
        random_num = randrange(len(old_list))

        while random_num in random_num_list:
            random_num = randrange(len(old_list))
        
        random_num_list.append(random_num)
        shuffled_list.append(old_list[random_num])

    return shuffled_list

def shuffle_in_place(unshuffled_list):
    # import randrange
    from random import randrange

    # variables
    random_num_list = []
   
    # for-loop
    for index in range(len(unshuffled_list) * 2):
        # variables
        random_num1 = randrange(len(unshuffled_list))
        random_num2 = randrange(len(unshuffled_list))

        random_item1 = unshuffled_list[random_num1] # must define variable here so it isn't change later

        # while-loop --> 
        while random_num1 == random_num2:
            random_num2 = randrange(len(unshuffled_list))
        
        # adjust variables
        unshuffled_list[random_num1] = unshuffled_list[random_num2]
        unshuffled_list[random_num2] = random_item1 # unshuffled_list[random_num2] = ORIGINAL value of unshuffled_list[random_num1]

    # return
    return unshuffled_list

def main():
    list_one = ["Jean Valjean", "Javert", "Fantine", "Cosette", "Marius Pontmercy", "Eponine", "Enjolras"]
    print("ORIGINAL LIST_ONE: {}".format(list_one))
    # First function execution
    print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))

    list_two = ["A", 0, 0, 5, 1, 3, 2]
    print("ORIGINAL LIST_TWO: {}".format(list_two))
    # Second function execution
    shuffle_in_place(list_two)
    print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))

main()
