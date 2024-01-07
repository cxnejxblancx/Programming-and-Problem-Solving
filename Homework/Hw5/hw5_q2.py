# inputs
sequence1 = input("Enter a DNA sequence: ")
sequence2 = input("Enter a second DNA sequence: ")

# variables
fused_sequence = ""
complement_sequence = ""
invalid_characters = 0

# conditonals
if len(sequence1) > len(sequence2):
    for char in range(len(sequence1)):
        if char < len(sequence2):
            fused_sequence += (sequence1[char] + sequence2[char])

        else:
            fused_sequence += sequence1[char]

elif len(sequence1) < len(sequence2):
    for char in range(len(sequence1)):
        if char < len(sequence1):
            fused_sequence += (sequence1[char] + sequence2[char])

        else:
            fused_sequence += sequence2[char]

else:
    for char in range(len(sequence1)):
            fused_sequence += (sequence1[char] + sequence2[char])

# for-loop
for char in fused_sequence:
    if (char == "A"):
        complement_sequence += "T"

    elif (char == "T"):
        complement_sequence += "A"

    elif (char == "C"):
        complement_sequence += "G"

    elif (char == "G"):
        complement_sequence += "C"

    else:
        invalid_characters += 1
        
# final prints
print("Fused sequence:", complement_sequence, end = " | ")
print("Invalid characters: " + str(invalid_characters))
