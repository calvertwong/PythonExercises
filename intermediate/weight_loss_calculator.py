# init variables
days = 1
accumulatedWeight = 0
averageWeight = 0
firstWeight = -1
lastWeight = -1
weight = 0

# Prompt user to enter weight 
while weight >= 0:
  weight = float(input(("Enter your weight on day " + str(days) + ": ")))
  # Store weight of day 1
  # lasWeight is being stored too just in case of user put in one weight only for the minus operation
  if days == 1: 
    firstWeight = weight
    lastWeight = weight
  
  if weight < 0:
    days -= 1 
  else:
    days += 1
    accumulatedWeight += weight
    lastWeight = weight

if firstWeight != -1:
  # Calculate average weight and total weight loss
  averageWeight = round((accumulatedWeight / days), 2)
  totalWeightLoss = round((firstWeight - lastWeight), 2)

  print("\nAverage Weight Over " + str(days) + " Days: " + "{:.2f}".format(averageWeight))
  print("Total Weight Loss Over " + str(days) + " Days: " + "{:.2f}".format(totalWeightLoss))