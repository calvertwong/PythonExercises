"""
Custom functions to print numbers and lines
"""

def horizontal_line(width, character):
  return width * character + '\n'

def vertical_line(shift, height, character):
  return (character.rjust(shift) + "\n") * height 

def two_vertical_line(width, height, character):
  return (character + character.rjust(width-1) + '\n') * height

def isOdd(num):
  return True if num % 2 != 0 else False

def number_0(width, character):
  return horizontal_line(width, character) + two_vertical_line(width, 3, character) + horizontal_line(width, character)

def number_1(width, character):
  return vertical_line(width, 5, character)

def number_2(width, character):
  return horizontal_line(width, character) + vertical_line(width, 1, character) + horizontal_line(width, character) + vertical_line(0, 1, character) + horizontal_line(width, character)

def number_3(width, character):
  return (horizontal_line(width, character) + vertical_line(width, 1, character)) * 2 + horizontal_line(width, character)

def number_4(width, character):
  return two_vertical_line(width, 2, character) + horizontal_line(width, character) + vertical_line(width, 2, character)

def number_5(width, character):
  return horizontal_line(width, character) + vertical_line(0, 1, character) + horizontal_line(width, character) + vertical_line(width, 1, character) + horizontal_line(width, character)

def number_6(width, character):
  return horizontal_line(width, character) + vertical_line(0, 1, character) + horizontal_line(width, character) + two_vertical_line(width, 1, character) + horizontal_line(width, character)

def number_7(width, character):
  return horizontal_line(width, character) + vertical_line(width, 4, character)

def number_8(width, character):
  return  (horizontal_line(width, character) + two_vertical_line(width, 1, character)) * 2 + horizontal_line(width, character)

def number_9(width, character):
  return  horizontal_line(width, character) + two_vertical_line(width, 1, character) + horizontal_line(width, character) + vertical_line(width, 2, character)

def print_number(num, width, character):
  number_functions = {
    0: number_0,
    1: number_1,
    2: number_2,
    3: number_3,
    4: number_4,
    5: number_5,
    6: number_6,
    7: number_7,
    8: number_8,
    9: number_9
  }
  print(number_functions[num](width, character))

def plus(width, character):
  if isOdd(width):
    return vertical_line(int(width / 2) + 1, 2, character) + horizontal_line(width, character) + vertical_line(int(width / 2 + 1), 2, character)
  else:
    return vertical_line(int(width / 2) + 1, 2, character * 2) + horizontal_line(width, character) + vertical_line(int(width / 2 + 1), 2, character * 2)

def minus(width, character):
  return horizontal_line(width, character)

def multiply(width, character):
  return two_vertical_line(width, 1, character) + " " + two_vertical_line(width - 2, 1, character) + vertical_line(int(width / 2 + 1) if width % 2 != 0 else int(width / 2), 1, character) + " " + two_vertical_line(width - 2, 1, character) + two_vertical_line(width, 1, character)

def divide(width, character):
  if isOdd(width):
    return vertical_line(int(width / 2) + 1, 1, character) + "\n" + horizontal_line(width, character) + "\n" + vertical_line(int(width / 2) + 1, 1, character)
  else:
    return vertical_line(int(width / 2) + 1, 1, character * 2) + "\n" + horizontal_line(width, character) + "\n" + vertical_line(int(width / 2) + 1, 1, character*2)

def check_answer(numOne, numTwo, answer, operator):
  if operator == '+':
    return True if numOne + numTwo == answer else False
  elif operator == '-':
    return True if numOne - numTwo == answer else False
  elif operator == '*':
    return True if numOne * numTwo == answer else False
  elif operator == '/':
    return True if numOne / numTwo == answer else False