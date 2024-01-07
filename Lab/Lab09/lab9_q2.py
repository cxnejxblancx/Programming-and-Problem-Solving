# PART A: Consecutive Numbers
def consecutive_numbers(filename, n):
    # create new file
    file_obj = open(filename, 'w')

    # for-loop
    for num in range (1, (n + 1)):
        print(num)
        
# PART B: Square Them
def squared_numbers(filename, outFile):
    # open old file
        # try-except
    try:
        existing_file = open(filename, 'r')

    except FileNotFoundError:
        print(f"The file '{existing_file}' doesm not exist.")
        return False
    
    # open newfile
    new_file = open(outFile, 'w')

    # for-loop 
    for line in existing_file:
        num = int(line.strip())
        num_squared = num ** 2

        print(num_squared, file = new_file)
        
    # close files
    new_file.close()
    existing_file.close()
        
    # return
    return outFile

def main():
    # Part A
    consecutive_numbers("numbers.txt", 5)

    # Part B
    squared_numbers("numbers.txt", "squaredNumbers.txt")

main()
        
