# weights
    # Highest exam (25%)
    # Second highest exam (20%)
    # Third highest exam (15%)
    # Homework (20%)
    # Lab (20%)

# input
highest_exam = int(input("Enter your highest exam grade: "))
second_highest_exam = int(input("Enter your second highest exam grade: "))
third_highest_exam = int(input("Enter your third highest exam grade: "))
average_homework = int(input("Enter your average homework exam grade: "))
average_lab = int(input("Enter your average lab grade: "))

# calculations
weight_heighest = (highest_exam * 0.25)
weight_second = (second_highest_exam * 0.2)
weight_third = (third_highest_exam * 0.15)
weight_homework = (average_homework * 0.2)
weight_lab = (average_lab * 0.2)

average_grade = weight_heighest + weight_second + weight_third + weight_homework + weight_lab

# conditionals
if average_grade > 92:
    letter_grade = "A"

elif 90 <= average_grade:
    letter_grade = "A-"

elif 87 <= average_grade:
    letter_grade = "B+"

elif 83 <= average_grade:
    letter_grade = "B"

elif 80 <= average_grade:
    letter_grade = "B-"

elif 77 <= average_grade:
    letter_grade = "C+"

elif 73 <= average_grade:
    letter_grade = "C"

elif 70 <= average_grade:
    letter_grade = "C-"

elif 67 <= average_grade:
    letter_grade = "D+"

elif 60 <= average_grade:
    letter_grade = "D"
    
else:
    letter_grade = "F"

# print
print("Your final grade is " + letter_grade)
