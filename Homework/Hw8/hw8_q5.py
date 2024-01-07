def get_matryoshka_list(original):
    # variables
    start = 0
    new_list = []
    ind_list = []
    
    # for-loop -- iterate through each index in the list
    for index in range((len(original))):
        # conditionals --> check that theres another index above the current one
        if index < (len(original) - 1):
            # conditionals --> check if first value less than the second value
            if original[start] < original[index + 1]:
                ind_list.append(original[index])
                start += 1

            else:
                ind_list.append(original[start])
                start = index + 1
                new_list.append(ind_list)
                ind_list = []
        
        else:
            ind_list.append(original[index])
            new_list.append(ind_list)

    # return
    return new_list
        

def main():
    # variables
    original_list = [1, 2, 3, 5, 20, 19, 3, 4, 7, 45, 100, 1, 3]
    matryoshka_list = get_matryoshka_list(original_list)   

    # final print
    print(matryoshka_list)

main()
