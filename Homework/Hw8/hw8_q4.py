def get_list_of_grades(grades_filepath):
    # open file
      # try-except
    try:
        file_obj = open(grades_filepath, 'r')

    except FileNotFoundError:
        # return --> end the function
        return

    # remove header and return a list of each line in the file
    file_obj.readline()

    # variables
    all_grades = []
    question_grades = []
    final_list = []
    total_grades = 0
    total_students = 0
    index = 0
  
    # for-loop --> iterate through each line in the file
    for student in file_obj:
      total_students += 1
      student = student.strip().split(',')[5:]
      # iterate through grades in each line
      for grade in student:
        total_grades += 1
        
      # adjust variable --> add all students' grades to one list
      all_grades += student
      
    # close file
    file_obj.close()
  
    # variable
    num_questions = int(total_grades / total_students)
    
    # for-loop --> separate grades based on corresponding question, create list of the lists of all grades for each question
    for num in range(num_questions):
      question_grades.append(list(all_grades[num::num_questions]))
      index += 1

    # for-loop --> create new list: cast grades as floats, get rid of empty grades
    for question in question_grades:
      actual_grades_for_question = []
      for student_score in question:
        # try-except
        try:
          actual_grades_for_question.append(float(student_score))
        except ValueError:
          continue

      # adjust variable
      final_list.append(list(actual_grades_for_question))

    # return
    return final_list


def generate_statistics_report(grades_filepath, stats_filepath = "score_stats.csv"):
    # variables
    grades_list = get_list_of_grades(grades_filepath)

    # open file in write mode
    new_file = open(stats_filepath, 'w')
    print("Mean,Standard Deviation,Median", file = new_file)    

    # for-loop --> sort each question
    for question_list in grades_list:
        # adjust list --> order from least to greatest
        question_list.sort() # sorting preferred, not necessary

        # variables
        total_distance = 0
        total_grades = 0
        sum_grades = 0

        # for-loop --> adjust variable
        for grade_item in question_list:
            total_grades += 1
            sum_grades += grade_item
          
        # try-except
        try:
          mean = round((sum_grades/ total_grades), 2)
        except ZeroDivisionError:
          mean = 0

        # conditonals --> calculate median if # grades even or odd
        if total_grades % 2 != 0: # if odd # of grades
            med_index = int(total_grades // 2)
            median = question_list[med_index]

        else: # if even # of grades
            # calculations --> find middle indices
            low_middle_index = int((total_grades / 2) - 1)
            high_middle_index = int(total_grades / 2)

            # variables --> values at middle indices
            med1 = question_list[low_middle_index]
            med2 = question_list[high_middle_index]
          
            # calculation --> median
            median = (med1 + med2) / 2

        # for-loop --> calculate square_distance for standard deviate
        for grade_item in question_list:
            # calculation --> squared distance from grade to the mean
            square_distance = (grade_item - mean) ** 2

            # adjust variable --> sum of squared distances for each grade
            total_distance += square_distance

        # calculation --> standard deviation
        stand_deviation = round(((total_distance / (total_grades - 1)) ** (1/2)), 2)
        

        # final-print --> print mean, standard deviation, and median each question on separate lines of the new file
        print(f"{mean},{stand_deviation},{median}", file = new_file)

    # return
    return new_file


def main():
    # variable
    generate_statistics_report("Midterm1_scores.csv", "stats.csv")

main()
