def update_frequencies(nucleotide_frequencies, dna_sequence):
    # import deepcopy
    from copy import deepcopy

    # variables
    added_adenine = 0
    added_thymine = 0
    added_cytosine = 0
    added_guanine = 0

    # for-loop
    for char in dna_sequence:
        if char == "A":
            added_adenine += 1
        elif char == "C":
            added_cytosine += 1
        elif char == "T":
            added_thymine += 1
        elif char == "G":
            added_guanine += 1
        
    # final print
    print(f"Number of nucleotides added: A -> {added_adenine} | C -> {added_cytosine} | T -> {added_thymine} | G -> {added_guanine}")

    # variables
    copy_of_frequencies = deepcopy(nucleotide_frequencies)
    updated_frequencies = []
    
    # for-loop
    for item in copy_of_frequencies:
        # variable
        item = list(item)

        # conditionals
        if item[0] == "A":
            item[1] += added_adenine
        elif item[0] == "T":
            item[1] += added_thymine
        elif item[0] == "C":
            item[1] += added_cytosine
        elif item[0] == "G":
            item[1] += added_guanine
        
        # adjust variable
        updated_frequencies.append(tuple(item))
        
    # return
    return updated_frequencies


def main():
    # variables
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTZGTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    # final print
    print(new_frequencies)

main()
