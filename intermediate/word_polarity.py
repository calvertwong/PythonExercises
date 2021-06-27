accumScore = 0
counter = 0
avgScore = 0

userInput = input("Enter a word to test: ")

try:
  reviewFile = open("movie_reviews.txt", "r")

  for line in reviewFile:
    if (" " + userInput + " ") in line.lower():
      accumScore += int(line[0])
      counter += 1

  if counter != 0:
    avgScore = accumScore / counter

  print("'" + userInput + "' appears " + str(counter) + " times")
  print("The average score for reviews containing the word '" + userInput + "' is " + str(avgScore) if counter != 0 else "There is no average score for reviews containing the word '" + userInput + "'")
  print("This is a positive word" if avgScore >= 2.0 else ("This is a negative word" if avgScore != 0 else "Cannot determine if this word is positive or negative"))

  reviewFile.close()
except:
  print("Error opening the file! Please check if you have the correct file name and path.")