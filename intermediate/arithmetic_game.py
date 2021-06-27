import Myfunctions
import random

# _______________________
#|  index  |  operation  | 
#|_________|_____________|
#|    0    |      +      |
#|_________|_____________|
#|    1    |      -      |
#|_________|_____________|
#|    2    |      *      |
#|_________|_____________|
#|    3    |      /      |
#|_________|_____________|

# Store the total number of generated questions by operations
operationsStats = [0, 0, 0, 0]
# Store the total number of questions answered correctly by operations 
correctnessListByOperations = [0, 0, 0, 0]
# Store the total number of attempts by operations
attemptListByOperations = [0, 0, 0, 0]

ADDER = 0
SUBTRACTOR = 1
MULTIPLIER = 2
DIVIDER = 3

OPERATORS = {
  0: '+',
  1: '-',
  2: '*',
  3: '/'
}

WORDS_DICT = {
  0: "addition",
  1: "subtraction",
  2: "multiplication", 
  3: "division"
}

FUNCTION_DICT = {
  0: Myfunctions.plus,
  1: Myfunctions.minus,
  2: Myfunctions.multiply, 
  3: Myfunctions.divide
}

# Get operands and operator
def get_operands_operator():
  randomOperator = random.randint(0, 3)
  numOne = random.randint(0, 9)
  numTwo = random.randint(0, 9)

  # Ensure that the question will get a whole number as the final number
  # Ensure that the divider is not 0
  if randomOperator == DIVIDER:
    while True:
      try:
        if numOne % numTwo == 0:
          break
        else:
          numOne = random.randint(0, 9)
          numTwo = random.randint(0, 9)
      except ZeroDivisionError:
        numOne = random.randint(0, 9)
        numTwo = random.randint(0, 9)

  return [numOne, numTwo, randomOperator]

# Print question
def print_question(numOfQuestions):
  for index in range(numOfQuestions):
    print("\nWhat is .....\n")

    expression = get_operands_operator()

    Myfunctions.print_number(num=expression[0], width=width, character=character)

    operationsStats[expression[2]] += 1
    print("\n\n" + FUNCTION_DICT[expression[2]](width=width, character=character) + "\n\n")

    Myfunctions.print_number(num=expression[1], width=width, character=character)

    answer = int(input("= "))

    if isDrillMode == 'yes':
      while not do_check(expression, answer):
        answer = int(input("= "))
    else:
      do_check(expression, answer)    

  if isDrillMode == "yes":
    print("\nThanks for playing!\n")
  else:
    print("\nYou got " + str(sum(correctnessListByOperations)) + " out of " + str(numOfQuestions) + " correct!\n")

# Check solution
def do_check(expression, answer):
  if Myfunctions.check_answer(numOne=expression[0], numTwo=expression[1], answer=answer, operator=OPERATORS[expression[2]]) == True:
    if expression[2] == ADDER:
      correctnessListByOperations[0] += 1
    elif expression[2] == SUBTRACTOR:
      correctnessListByOperations[1] += 1
    elif expression[2] == MULTIPLIER:
      correctnessListByOperations[2] += 1
    elif expression[2] == DIVIDER:
      correctnessListByOperations[3] += 1
    print("Correct!")
    return True
  else:
    if isDrillMode:
      if expression[2] == ADDER:
        attemptListByOperations[0] += 1
      elif expression[2] == SUBTRACTOR:
        attemptListByOperations[1] += 1
      elif expression[2] == MULTIPLIER:
        attemptListByOperations[2] += 1
      elif expression[2] == DIVIDER:
        attemptListByOperations[3] += 1
    print("Sorry, that's not correct.")
    return False

# Print statistics
def print_stats(stats, correctProblemsByOperation, correctPercentByOperation, attemptsByOperation):
  for index in range(len(stats)):
    if stats[index] == 0:
      print("No " + WORDS_DICT[index] + " problems presented\n")
    else:
      print("Total " + WORDS_DICT[index] + " problems presented:  " + str(stats[index]))
    
    if isDrillMode == "no" and stats[index] != 0:
      print("Correct " + WORDS_DICT[index] +" problems: " + str(correctProblemsByOperation[index]) + " (" + str(round(correctPercentByOperation[index] * 100, 1)) + "%)\n")
    elif isDrillMode == "yes" and stats[index] != 0:
      print("# of extra attempts needed: " + str(attemptsByOperation[index]) + (" (perfect)\n" if attemptsByOperation[index] == 0 else "\n"))

# Start of the program
while True:
  try:
    numOfQuestions = int(input("How many problems would you like to attempt? "))
    if numOfQuestions > 0:
      break
    else:
      print("Invalid number, try again")
  except ValueError:
    print("Invalid input, try again")

while True:
  try:
    width = int(input("How wide do you want your digits to be? 5-10: "))
    if width >= 5 and width <= 10:
      break
    else:
      print("Invalid width, try again")
  except ValueError:
    print("Invalid input, try again")

while True:
  character = input("What character would you like to use? ")
  if len(character) == 1:
    break
  else:
    print("String too long, try again")

while True:
  isDrillMode = input("Would you like to activate 'drill' mode? yes or no: ")
  if isDrillMode == "yes" or isDrillMode == 'no':
    break
  else:
    print("Invalid input, try again")

print("\nHere we go!")

print_question(numOfQuestions)

print_stats(operationsStats, correctnessListByOperations, [correctnessListByOperations[index] / operationsStats[index] if correctnessListByOperations[index] != 0 else 0 for index in range(len(correctnessListByOperations))], attemptListByOperations)