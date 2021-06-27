import math

def primeNumbersDetector(n):
  primeNumberList = []
  indicatorList = ['P']*n
  indicatorList[0] = indicatorList[1] = 'N'
  currentIndex = 2
  newLineCounter = 1
  # improve efficiency by not checking everything
  stopper = int(math.sqrt(n))

  # set multiple of numbers to 'N
  while currentIndex < stopper:
    if indicatorList[currentIndex] == 'P':
      for index in range(currentIndex+currentIndex, n, currentIndex):
        indicatorList[index] = 'N'
    
    currentIndex+=1

  # Print output
  for index in range(len(indicatorList)):
    if indicatorList[index] == 'P':
      if newLineCounter % 10 == 0:
        print(str(index).rjust(len(str(n))), end="\n")
      else:
        print(str(index).rjust(len(str(n))), end=" ")

      newLineCounter+=1


while(True):
  num = int(input("Enter an integer greater than or equal to 10: "))
  if num >= 10:
    primeNumbersDetector(num+1)
    break

