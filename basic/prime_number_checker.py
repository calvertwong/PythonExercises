# prime checker
"""
given a number
determine if the number is prime
a number is prime if and only if the only divisors it has are 1 and itself
2 3 5 7 11 13 ...
"""

number = int(input("Please enter a number to check: "))
num_divisors = 0
d = 1
while d <= number:
    if number % d == 0:
        num_divisors += 1
    d += 1

if num_divisors == 2:
    print(number, "is prime!")
else:
    print(number, "is not prime.")