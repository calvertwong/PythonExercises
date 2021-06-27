ERROR_MSG = {
  0: "I don't understand that ...\n\n",
  1: "Invalid, try again"
}

OPERATIONS_TEXTS = {
  1: "\nAll prime numbers between ",
  2: "\nAll perfect numbers between ",
  3: "\nAll abundant numbers between "
}

def is_even(num):
  return True if num % 2 == 0 else False

def is_odd(num):
  return True if num % 2 != 0 else False

def is_prime(num):
  if num > 1:
    for i in range(2, num):
      if num % i == 0:
        return False
  else:
    return False

  return True

def is_perfect(num):
  sum = 0
  
  for factor in range(1, num):
    if num % factor == 0:
      sum += factor
  return num == sum

def is_abundant(num):
  return sum([factor for factor in range(1, num) if num % factor == 0]) > num

FUNCTION_DICT = {
  1: is_prime,
  2: is_perfect,
  3: is_abundant,
  4: is_even,
  5: is_odd
}

# Print result
def print_result(userInput, startNum, endNum):
  def get_result_helper(whichFunction):
    result = []

    # Call the even, odd, prime, perfect, abundant operations 
    for num in range(startNum, endNum + 1):
      if FUNCTION_DICT[whichFunction](num):
        result.append(num)
    
    return result if result != [] else []

  if userInput < 4:
    print(OPERATIONS_TEXTS[userInput] + str(startNum) + " and " + str(endNum) + "\n##############")
    print(*get_result_helper(userInput), sep = "\n")
    print("##############\n")
  elif userInput == 4:
    print("\nNumber".ljust((len(str(endNum)) if len(str(endNum)) > 6 else 6) + 4) + "Even".ljust(10) + "Odd".ljust(10) + "Prime".ljust(10) + "Perfect".ljust(10) + "Abundant".ljust(10))
    evenList = get_result_helper(4)
    oddList = get_result_helper(5)
    primeList = get_result_helper(1)
    perfectList = get_result_helper(2)
    abundantList = get_result_helper(3)

    for num in range(startNum, endNum + 1):
      print(str(num).ljust((len(str(endNum)) if len(str(endNum)) > 6 else 6) + 2),
      "x".ljust(9) if num in evenList else "".ljust(9),
      'x'.ljust(9) if num in oddList else "".ljust(9),
      'x'.ljust(9) if num in primeList else "".ljust(9), 
      'x'.ljust(9) if num in perfectList else "".ljust(9), 
      'x' if num in abundantList else ''
      )

# Start of the program
startNum = 0
endNum = 0

while True:
  print("Main Menu\n\n1 - Find all prime numbers within a given range\n2 - Find all perfect numbers within a given range\n3 - Find all abundant numbers within a given range\n4 - Chart all even, odd, prime, perfect and abundant numbers within a given range\n5 - Quit\n")

  try:
    userInput = int(input("Your choice: "))

    if userInput >= 1 and userInput <= 4:
      while True:
        try:
          startNum = int(input("Enter starting number (positive only): "))

          if startNum > 0:
            while True:
              endNum = int(input("Enter ending number: "))

              if endNum >= startNum:
                print_result(userInput, startNum, endNum)
                break
              else:
                print(ERROR_MSG[1])
          else:
            print(ERROR_MSG[1])
        except ValueError:
          print(ERROR_MSG[1])
        else:
          if endNum > 0:
            endNum = 0
            break
    elif userInput == 5:
      print("Goodbye!")
      break
    else:
      print(ERROR_MSG[0])
  except ValueError:
    print(ERROR_MSG[0])

