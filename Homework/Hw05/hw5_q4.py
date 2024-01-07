# input
encoded = input("Enter an encoded string: ")
key = int(input("Enter a key: "))

# variables
decoded = ""

# for-loop
for char in encoded[-1::(-(key + 1))]:
    if not char.isdigit():
        decoded += char

# final print
print("Your message is '" + decoded + "'") 
