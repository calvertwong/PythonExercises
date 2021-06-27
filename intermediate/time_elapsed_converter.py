# Init variables
isTimeValid = True
timeInput = 0

while isTimeValid:
  timeInput = int(input("Please enter the number of seconds elapsed: "))
  if timeInput >= 0:
    hours = int(timeInput / 3600)
    minutes = int((timeInput - hours * 3600) / 60)
    seconds = int((timeInput - hours * 3600 - minutes * 60))
    print(str(hours) + " hours, " + str(minutes) +  " minutes, " + str(seconds) + " seconds")
  else:
    isTimeValid = False
    print("Exiting program...")
