# pre-print
print("Please enter your secret message:")

# input
original = input("")

# variable
ind_word = ""
secret = ""

for char in range(len(original)):
    if original[char] == " ":
        ind_word = original[:char]
        original = original[char + 1:]
        if 65 <= ord(ind_word[0]) <= 90:
            secret += ind_word[0]
        
