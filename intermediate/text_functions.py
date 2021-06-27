# a) Using .format() function to convert integer to string
def stringify_digit(digit):
  return '{}'.format(digit)

# b) Reverse string using a slice that steps backwards
def reverse(text):
  return text[::-1]

# c) Since this requirement is the same as (a), I am calling function from (a) to get the result
def stringify(num):
  return stringify_digit(num)

print(stringify_digit(9))
print(reverse("Hello"))
print(stringify_digit(-234))