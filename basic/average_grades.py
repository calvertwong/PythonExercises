# grades
"""
ask the user to enter grades until they enter -1
compute the average of all the grades entered
"""
grade = 0

# sentinel
sentinel = -1

# accumulator
total = 0
count = 0
while grade != sentinel:
    grade = int(input("Please enter a grade or -1 to stop: "))
    if grade == sentinel:
        break
    total += grade
    count += 1
if count > 0:
    print(total/count)
else:
    print("No valid grades were entered")