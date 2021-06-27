print("Instructions: Please enter three strings.")

# Empty string list
stringList =[]

# Prompt user for 3 strings inputs
stringOne = input("Enter the first string: \t")
stringTwo = input("Enter the second string:\t")
stringThree = input("Enter the third string: \t")

# Add user inputs into a list
stringList.append(stringOne)
stringList.append(stringTwo)
stringList.append(stringThree)

# String methods to sort and achieve the required requirements
# Refer: https://www.geeksforgeeks.org/python-ways-to-sort-list-of-strings-in-case-insensitive-manner/
stringList.sort()
stringList.sort(key = lambda x: x.lower())

print("\nHere are the strings in ascending alphabetical order:")

print(stringList[0])
print(stringList[1])
print(stringList[2])

