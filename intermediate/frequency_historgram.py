largest = -1
smallest = -1
dict = {}
mode = 0

userInput = input("Enter a series of numbers separated by spaces: ")

inputList = userInput.split()

for item in inputList:
  try:
    num = int(item)

    if largest == -1:
      largest = num
    if smallest == -1:
      smallest = num

    if num < 0 or num > 10:
      print("* " + item + " is out of bounds - rejecting")
    else:
      print("* " + item + " is valid - accepting" )
      if item in dict:
        dict[item] += 1
      else:
        dict[item] = 1

    if num > largest:
      largest = num
    if num < smallest: 
      smallest = num
  except:
    print("* " + item + " is not a number" )

for key in dict:
  if dict[key] > mode:
    mode = dict[key]

print("Largest number: " + str(largest))
print("Smallest number: " + str(smallest))
print("Range of values: " + str(largest - smallest))
print("Mode: " + str(mode))
print("Frequecy Histogram:")
for key in dict:
  print(key + " " + "#" * int(dict[key]))

