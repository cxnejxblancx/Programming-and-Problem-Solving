def create_error_log(dna_sequence, file_pathway):
    # open error log
    error_log = open("error_log.txt", 'w')
  
    # open file
    try:
        indices_file = open(file_pathway, 'r')

    except FileNotFoundError:
        # write into error log; close file
        print("FILENOTFOUNDERROR: The file specified was not found or could not be opened.", file = error_log)
        error_log.close()

    # variable
    line_num = 0

    # iterate through each line in the file
    for line in indices_file:
        line_num += 1
        index = line.strip()

        try:
            index = int(index)

        except ValueError:
            print(f"VALUEERROR at LINE {line_num}: The value read, '{index}', cannot be casted into an integer to be used as an index.", file = error_log)

        else:
            try:
                corrupted_nucleotide = dna_sequence[index]

            except IndexError:
                print(f"INDEXERROR at LINE {line_num}: The value read, {index}, is larger than the sequence length of {len(dna_sequence)}.", file = error_log)

        # close files
        error_log.close()
        indices_file.close()

        # return
        return error_log


def main():
    # function call
    create_error_log("ACTGC AXT", 'indices.txt')

main()
