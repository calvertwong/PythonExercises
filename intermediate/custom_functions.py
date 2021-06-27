def listlen(inputList):
  count = 0
  for c in inputList:
    count+=1
  return count

def listmax(inputList):
  largest = inputList[0]
  for item in inputList:
    if item > largest:
      largest = item
  return largest

def listcopy(inputList):
  copiedList = []

  if inputList != []: 
    for item in inputList:
      copiedList = copiedList + [item]
      
  return copiedList

def listappend(inputList, value):
  inputList = inputList + [value]
  return inputList

def listinsert(inputList, inputIndex, value):
  inputList = inputList[:inputIndex] + [value] + inputList[inputIndex:]
  return inputList

def listremove(inputList, value):
  removeIndex = 0

  for index in range(len(inputList)):
    if inputList[index] == value:
      removeIndex = index
  inputList = inputList[:removeIndex] + inputList[removeIndex + 1:]
  return inputList

def listreverse(inputList):
  tempList = []
  
  for index in range(len(inputList)-1, -1, -1):
    tempList = tempList + [inputList[index]]
  return tempList

# function callers
sampleListOne = [10, 20, 30]
sampleListTwo = [10, 20, 30, 5, 3]

print("----listlen----")
print(listlen(sampleListOne))
print("\n")

print("----listmax----")
print(listmax(sampleListTwo))
print(sampleListTwo)
print("\n")

print("----listcopy----")
print(listcopy(sampleListOne))
print("\n")

print("----listappend----")
print(listappend(sampleListOne, 999))
print("\n")

print("----listinsert----")
print(listinsert(sampleListOne, 1, 999))
print(sampleListOne)
print("\n")

print("----listremove----")
print(listremove(sampleListOne, 20))
print(sampleListOne)
print("\n")

print("----listreverse----")
print(listreverse(sampleListOne))
print(sampleListOne)