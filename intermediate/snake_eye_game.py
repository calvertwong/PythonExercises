import random

# Constants
validSidesList = [4, 6, 8, 10, 12, 20]

# Init variables
isValidSide = False
accumulatedDiceOne = 0.0
accumulatedDiceTwo = 0.0
numOfRolls = 1
rolledDoubles = 1
lowerBound = 1
upperBound = 0
isSnakeEyes = False

# Prompt user to get a valid input, ask again if the input is invalid
while not isValidSide:
  sidesInput = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
  if validSidesList.__contains__(sidesInput):
    print("\nThanks! Here we go ...")
    isValidSide = True
    upperBound = sidesInput
  else:
    print("Sorry, that's not a valid size.\n")

while not isSnakeEyes:
  diceOneValue = random.randint(lowerBound, upperBound)
  diceTwoValue = random.randint(lowerBound, upperBound)

  accumulatedDiceOne += diceOneValue
  accumulatedDiceTwo += diceTwoValue

  print(str(numOfRolls) + ". dice number 1 is " + str(diceOneValue) + " and dice number 2 is " + str(diceTwoValue) + ".")

  # Do this when snake eye
  if diceOneValue == 1 and diceTwoValue == 1:
    rolledDoublesPercentage = round(rolledDoubles / numOfRolls *100, 2)
    print("\nYou got snake eyes! Finally! On try number " + str(numOfRolls) + "!")
    print("Along the way you rolled doubles " + str(rolledDoubles) + " times (" + "{:.2f}".format(rolledDoublesPercentage) + "% of all rolls were doubles)")
    isSnakeEyes = True
  # Record the occurences of rolled doubles when not snake eye
  else:
    if diceOneValue == diceTwoValue:
      rolledDoubles += 1

  # Increment number of rolls
  numOfRolls += 1

# Calculate avg of both dices
avgDiceOne = round(accumulatedDiceOne / numOfRolls, 2)
avgDiceTwo = round(accumulatedDiceTwo / numOfRolls, 2)

print("The average roll for dice #1 was " + "{:.2f}".format(avgDiceOne))
print("The average roll for dice #2 was " + "{:.2f}".format(avgDiceTwo))