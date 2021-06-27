# Init variable
primeList = []

# Prompt user inputs
startNum = int(input("Start number: "))
endNum = int(input("End number: "))

# Determine how much space should be given to a number to right align numbers
numSpacing = len(str(endNum))

# Store prime number in a list
for num in range(startNum, endNum + 1):
  num_divisors = 0
  divisor = 1
  while divisor <= num:
      if num % divisor == 0:
          num_divisors += 1
      divisor += 1

  if num_divisors == 2:
      primeList.append(num)

# Output
for index, prime in enumerate(primeList):
  print(str(prime).rjust(numSpacing), end='  ')
  if (index + 1) % 10 == 0:
    print("\n")    
