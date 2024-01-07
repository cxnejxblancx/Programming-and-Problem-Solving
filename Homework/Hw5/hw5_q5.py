# import arpeggiator.py file
import arpeggiator

# arpeggiator module documentation
ARPEGGIATOR = arpeggiator.Arpeggiator()
UP = arpeggiator.Direction.UP
DOWN = arpeggiator.Direction.DOWN

# input
musical_note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

# while-loop
while musical_note != "DONE":
    ARPEGGIATOR.add_note(musical_note)
    musical_note = input("Enter a musical note (i.e. A, Db, C#, etc.) or 'DONE' to end: ")

# SEPARATE
print()
print(ARPEGGIATOR)
print()

# variable
direction = input("Enter an arpeggiator direction [U/D] ")

# while-loop
while (direction != 'D') and (direction != 'U'):
    direction = input("Enter an arpeggiator direction [U/D] ")

# SEPARATE
print()

# variable
iterations = int(input("How many times do you want your arpeggiator to play? "))

# while-loop
while iterations <= 0:
    iterations = int(input("How many times do you want your arpeggiator to play? (Must be positive amount) "))

# SEPARATE
print()

# for-loop
for iteration in range(iterations):
    if direction == "U":
        ARPEGGIATOR.play(UP)
        
    else:
        ARPEGGIATOR.play(DOWN)
  
