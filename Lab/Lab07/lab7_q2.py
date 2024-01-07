###### PART A
# input
phrase = input("Enter your phrase: ")

# final print
print(phrase[::-1])


###### PART B
# input
phrase = input("Enter your phrase: ")

# for-loop
for char in range(len(phrase) - 1, -1, -1):
    print(phrase[char], end = "")
  
