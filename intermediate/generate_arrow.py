# Init variables
space = " "
isInputValid = False
numOfCols = 0
numOfSpacing = 0

# Prompt user for a valid input
while not isInputValid:
  numOfCols = int(input("How many columns? "))
  if numOfCols >= 0:
    isInputValid = True
  else:
    print("Invalid entry, try again!")

arrowDirection = input("Enter direction (left or right): ")

# Print first half of the arrow (right direction)
if numOfCols > 0 and arrowDirection == "right":
  while numOfSpacing != numOfCols:
    print(numOfSpacing * space + "*")
    numOfSpacing += 1
  numOfSpacing -= 2

# Print second half of the arrow (right direction)
if numOfSpacing != 0 and arrowDirection == "right":
  while numOfSpacing != -1:
    print(numOfSpacing * space + "*")
    numOfSpacing -= 1

# Print first half of the arrow (left direction)
if numOfCols > 0 and arrowDirection == "left":
  numOfSpacing = numOfCols - 1
  while numOfSpacing != 0:
    print(numOfSpacing * space + "*")
    numOfSpacing -= 1

# Print second half of the arrow (left direction)
if numOfSpacing != numOfCols and arrowDirection == "left":
  while numOfSpacing != numOfCols:
    print(numOfSpacing * space + "*")
    numOfSpacing += 1
