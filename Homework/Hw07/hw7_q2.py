def get_root_of_average(file_pathway, root = 2):
    # open file
    try:
        file_obj = open(file_pathway, 'r')
    
    except FileNotFoundError:
        # print
        print(f"WARNING: The file pathway '{file_pathway}' does not exist.")

        # return
        return 0
    
    # sort through line
    for line in file_obj:
        # adjust --> strip line to avoid empty characters
        line = line.strip()
      
        # variables
        start = 0
        sum = 0
        total_nums = 0
        
        # for-loop --> separate string into individual nums and calculate the root of the average
        for index in range(len(line)):
            if line[index] == " " or line[index] == "\n":
                # # variables
                stop = index
                num = line[start:stop]
                start = stop + 1

                try:
                    num = float(num)

                except ValueError:
                    # print
                    print(f"WARNING: Could not cast '{num}' into a float.")

                else:
                    # adjust variables
                    sum += num
                    total_nums += 1

        # calculations
            # watch out for potential of dividing by zero when calculating average
        try:
            average = sum / total_nums

        except ZeroDivisionError:
            return 0
        
        root_of_average = average ** (1 / root)

        # close file
        file_obj.close()
        
        # return
        return root_of_average
                

def main():
    # variable
    cubed_root = get_root_of_average("numbers.txt", 3)

    # final print
    print(cubed_root)

main()
