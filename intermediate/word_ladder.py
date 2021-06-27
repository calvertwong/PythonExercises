stringAccum = ""
currentWord = ""
hasWon = False

def differ_by_one(currentWord, nextWord):
  difference = 0

  # check if the input next word is in the accumulated string
  if nextWord not in stringAccum.split():
    return False
  else:
    charList = []
    # check if the two words are differed by 1 character
    for i in range(len(currentWord)):
      charList.append(currentWord[i])
    
    for i in range(len(nextWord)):
      if nextWord[i] not in charList:
        difference += 1

    return difference == 1

# Program starts here
print("Welcome to word ladder!")

# Get user input
currentWord = input("Please enter the initial word: ")
goalWord = input("Please enter the goal word: ")
stringAccum += currentWord + " "
stringAccum += goalWord + " "

print("Asking for valid words...")

while True:
  # Get valid words
  validWord = input("Please enter a valid word: ")

  if validWord == "":
    break
  else:
    stringAccum += validWord + " "

# Get the number of accumulated string
wordCount = len(stringAccum.split())

print("Beginning game...")

while True:
  if wordCount == 0:
    break
  else:
    print("Current word is " + currentWord + ".\nYou have " + str(wordCount) + " attempt(s) to get to the goal word.")
    
    nextWord = input("Please enter next word: ")

    if differ_by_one(currentWord, nextWord):
      print("That is a valid word!")
      currentWord = nextWord
      if nextWord == goalWord:
        hasWon = True
        break
    else:
      print("Sorry that is not a valid word.")
      
    wordCount -= 1

if hasWon:
  print("Victory!")
else:
  print("Loser!")