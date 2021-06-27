"""
Write a program that given a temperature in Farenheit
Output the temperature in Celsius (rounded to 2 decimal places)
Continue to ask the user for a temperature until they enter "no"
C = 5/9 * (F-32)
"""
temperature = ""
while True:
    temperature = input("Please enter a temperature in F or 'no' to stop: ")
    if temperature == "no":
        break
    else:
        celsius = 5/9 * (float(temperature) - 32)
        print(str(format(celsius, ".2f")) + " C")
    
