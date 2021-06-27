# Init variables
numOfStudents = 0
numOfTests = 0
studentIndex = 1
testIndex = 1
testScore = -1
individualTotalScore = 0
classTotalScore = 0

# Prompt user for number of students, input must be a positive number
while numOfStudents <= 0:
  numOfStudents = int(input("How many students are in your class? "))
  if numOfStudents <= 0:
    print("Invalid # of students, try again.\n")

# Prompt user for number of tests, input must be a positive number
while numOfTests <= 0:
  numOfTests = int(input("How many tests in this class? "))
  if numOfTests <= 0:
    print("Invalid # of tests, try again.\n")

print("\nHere we go!\n")

for studentIndex in range(numOfStudents):
  print("**** Student #" + str(studentIndex + 1) + "****")

  for testIndex in range(numOfTests):
    while testScore < 0:
      testScore = float(input("Enter score for test #" + str(testIndex + 1) + ": "))
      if testScore < 0.0:
        print("Invalid score, try again")
      else:
        individualTotalScore += testScore
    
    testScore = -1

  avgScore = round(individualTotalScore / numOfTests, 2)
  print("Average score for student #" + str(studentIndex + 1) + " is " + "{:.2f}".format(avgScore) + "\n")
  classTotalScore += avgScore
  individualTotalScore = 0

print("Average score for all students is: " + "{:.2f}".format(round(classTotalScore / numOfStudents, 2)))

  