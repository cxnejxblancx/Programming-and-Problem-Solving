# input
phrase = input("Enter a phrase: ")

# varible
start = 0
word = ""
hidden_string = ""

# indexing
for char in range(len(phrase)):
    if char == " ":
        word = phrase[start: char]
        start = char + 1

        if word.isdigit():
            hidden_string += ("x" * len(word))
        else:
            hidden_string += (word + " ")
          
    print(hidden_string)
  
