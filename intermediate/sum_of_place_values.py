# Ask user for the first value
numOne = int(input("\nEnter value 1: "))

# Ask user for the second value
numTwo = int(input("Enter value 2: "))

print("\nPlace Value Totals:\n")

# Use modulo to get the last digit of a value
print("\t%d + %d = %d one(s)"%((numOne % 10, numTwo % 10, numOne % 10 + numTwo % 10)))

# Divide the number by 10 and use modulo to get the last digit of a value of tens place
print("\t%d + %d = %d ten(s)"%(((numOne // 10) % 10, (numTwo // 10) % 10, (numOne // 10) % 10 + (numTwo // 10) % 10)))

# Divide the number by 100 and use modulo to get the last digit of a value of hundreds place
print("\t%d + %d = %d hundred(s)"%(((numOne // 100) % 10, (numTwo // 100) % 10, (numOne // 100) % 10 + (numTwo // 100) % 10)))

# Divide the number by 1000 and use modulo to get the last digit of a value of thousands place
print("\t%d + %d = %d thousand(s)"%(((numOne // 1000) % 10, (numTwo // 1000) % 10, (numOne // 1000) % 10 + (numTwo // 1000) % 10)))





