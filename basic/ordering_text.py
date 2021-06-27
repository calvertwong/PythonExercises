# input() is used to prompt the user for input and the user input will be stored in a variable
nameOne = input("Please enter name 1: ")
nameTwo = input("Please enter name 2: ")
nameThree = input("Please enter name 3: ")

# Display a header
# Insert a new line with \n
print("\nHere are your names in every possible order:\n--------------------------------------------\n")

# Display all possible arrangements
# Concatenate strings with the element '+'
print("1.", nameOne + ", " + nameTwo + ", " + nameThree + "\n")
print("2.", nameOne + ", " + nameThree + ", " + nameTwo + "\n")
print("3.", nameTwo + ", " + nameOne + ", " + nameThree + "\n")
print("4.", nameTwo + "\n" + nameThree + "\n" + nameOne + "\n")
print("5.", nameThree + "\n" + nameTwo + "\n" + nameOne + "\n")
print("6.", nameThree + "\n" + nameOne + "\n" + nameTwo + "\n")