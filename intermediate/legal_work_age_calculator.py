print("Instructions: Enter the start date and birthdate for an employee\nto determine their age at the start of employment.")

# Month list in words
monthsInWords = ["January ", "February ", "March ", "April ", "May ", "June ", "July ", "August ", "September ", "October ", "November ", "December "]

# Day label list in words
dayLabel = ""

# Prompt the user to input a start date and birth date
startDate = int(input("Enter start date MMDDYYYY: "))
birthDate = int(input("Enter birth date MMDDYYYY: "))

# Math operations to extract the year, month, and day
startDateInYear = startDate % 10000
startDateInDay = (startDate // 10000) % 100
startDateInMonth = (startDate // 1000000) % 100

birthDateInYear = birthDate % 10000
birthDateInDay = (birthDate // 10000) % 100
birthDateInMonth = (birthDate // 1000000) % 100

# Determine the label for the day
if birthDateInDay == 1 or birthDateInDay == 21:
  dayLabel = "st, "
elif birthDateInDay == 2 or birthDateInDay == 22:
  dayLabel = "nd, "
elif birthDateInDay == 3 or birthDateInDay == 23:
  dayLabel = "rd, "
else:
  dayLabel = "th, "

print("The contestant was born on " + monthsInWords[birthDateInMonth - 1] + str(birthDateInDay) + dayLabel + str(birthDateInYear))

# Eligible if year is more than 21, else not eligible
if startDateInYear - birthDateInYear > 21:
  print("ELIGIBLE: The contestant will be 21 by the time taping begins")
# Check the start and birth day if year is 21, if start day is later than birth day then eligible, else not eligible
elif startDateInYear - birthDateInYear == 21:
  if startDateInDay > birthDateInDay or startDateInDay == birthDateInDay:
    print("ELIGIBLE: The contestant will be 21 by the time taping begins")
  else:
    print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")
else:
  print("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")