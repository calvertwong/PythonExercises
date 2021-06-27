# Grade of assignment 1
assignmentOneGrade = float(input("Enter assignment #1 grade:  "))

# Grade of assignment 2
assignmentTwoGrade = float(input("Enter assignment #2 grade:  "))

# Grade of assignment 3
assignmentThreeGrade = float(input("Enter assignment #3 grade:  "))

# Grade of weekly quizzes
weeklyQuizzesGrade = float(input("Enter weekly quizzes grade: "))

# Grade of midterm
midtermGrade = float(input("Enter midterm grade:        "))

# Grade of final exam
finalExamGrade = float(input("Enter final exam grade:     "))

# Calcalte assignments average
avgAssignmentGrade = (assignmentOneGrade + assignmentTwoGrade + assignmentThreeGrade) / 3

# Calculate final grade
finalGrade = avgAssignmentGrade * 0.25 + weeklyQuizzesGrade * 0.05 + midtermGrade * 0.25 + finalExamGrade * 0.45

# Print average assignment grade
print("\nAverage Assignment Grade:   " + str(avgAssignmentGrade))

# Print final grade formatted to 1 decimal place
print("\nFinal Grade:                " + "{:.1f}".format(finalGrade))

# Print True if final grade is 95 and above, print False lower than 95 
print("Is an A?                   ", "True" if finalGrade >= 95 else "False")
