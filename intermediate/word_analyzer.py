import time

words = {}
uniqueWordCounter = 0
accumWordAvgScore = 0

startTime = time.time()

print("Initializing sentiment database")

try:
  reviewFile = open("movie_reviews.txt", "r")

  for line in reviewFile:
    for word in line.lower().split():
      if word in words:
        words[word] = [words[word][0] + int(line[0]), words[word][1] + 1]
      else:
        uniqueWordCounter += 1
        words[word] = [int(line[0]), 1] 

  endTime = time.time()

  print("Sentiment database initialization complete\nTotal unique words analyzed: " + str(uniqueWordCounter) + "\nAnalysis took " + str(round(endTime - startTime, 2)) + " seconds to complete")

  userPhrase = input("\nEnter a phrase to test: ")

  wordList = userPhrase.lower().split()
  for word in wordList:
    if word in words.keys():
      wordAvgScore = words[word][0] / words[word][1]
      accumWordAvgScore += wordAvgScore
      print("* '" + word + "' appears " + str(words[word][1]) + " times with an average score of " + str(wordAvgScore))
    else:
      print("* '" + word + "' does not appear in any moview reviews")

  phraseAvgScore = accumWordAvgScore / len(wordList)
  if phraseAvgScore != 0:
    print(("Average score for this phrase is " + str(phraseAvgScore)))
  print("This is a POSITIVE phrase" if phraseAvgScore >= 2.0 else ("This is a NEGATIVE phrase" if phraseAvgScore != 0 else "Not enough words to determine sentiment."))

  reviewFile.close()
except:
  print("An error has occurred")