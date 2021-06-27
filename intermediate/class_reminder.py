# Constants
NUM_OF_MONTHS = 12
NUM_OF_DAY_EACH_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
CLASS_START_DAY = 2
CLASS_END_DAY = 21

classMonths = [9, 10, 11, 12]
classDays = [[3, 8, 10, 15, 17, 22, 24, 29], [1, 6, 8, 13, 15, 20, 22, 27, 29], [3, 5, 10, 12, 17, 19, 24], [1, 3, 8, 10]]

# Prompt user for a date
classInputDate = int(input("Enter a date in YYYYMMDD format (i.e. 20200903 for September 3rd, 2020): "))

# Math operations to extract the year, month, and day
inputDay = classInputDate % 100
inputMonth = (classInputDate // 100) % 100
inputYear = classInputDate // 10000

# Check if the input month and day are valid
if inputMonth > NUM_OF_MONTHS or inputDay > NUM_OF_DAY_EACH_MONTH[inputMonth - 1]: 
  print("That's not a valid date!")
# Check if the input date is before the start of the semester
elif inputMonth <= classMonths[0] and inputDay < CLASS_START_DAY:
  print("This date is before the semester begins")
# Check if the input date is after the semester ends
elif inputMonth == classMonths[3] and inputDay > CLASS_END_DAY: 
  print("This date is after the semester ends")
else:
  # Get the location of the input month in the classMonths list to be use in the next step
  foundMonthIndex = 0
  for monthIndex in range(len(classMonths)):
    if inputMonth == classMonths[monthIndex]:
      foundMonthIndex = monthIndex

  # Check if class will be held on the input day
  for dayIndex in range(len(classDays[foundMonthIndex])):
    if inputDay == classDays[foundMonthIndex][dayIndex]:
      print("You have class today")
      break
    elif dayIndex == len(classDays[foundMonthIndex]) - 1:
      print("You do not have class today")