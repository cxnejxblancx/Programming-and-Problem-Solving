# input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# variables
original_string = "cat"
hamming1 = 0
hamming2 = 0

# for-loop
for char in range(len(original_string)):
    if original_string[char] != str1[char]:
        hamming1 += 1
    if original_string[char] != str2[char]:
        hamming2 += 1

# finalprints
print('"' + str(original_string) + '" and "' + str(str1) + '" Hamming distance is ' + str(hamming1))
print('"' + str(original_string) + '" and "' + str(str2) + '" Hamming distance is ' + str(hamming2))
