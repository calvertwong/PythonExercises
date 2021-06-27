# Constant
SLICES_PER_PIZZA = 8

# Init variables
totalSlicesNeeded = 0
personIndex = 1
wholePizzaNeeded = 0
slizePizzaNeeded = 0
totalCost = 0
remainingMoney = 0

# Prompt user for inputs
budget = int(input("Enter budget for your party: "))
costPerSlice = float(input("Cost per slice of pizza: "))
costWholePizza = float(input("Cost per whole pizza pie (8 slices): "))
numOfPerson = int(input("How many people will be attending your party? "))

while personIndex <= numOfPerson:
  numOfSlices = int(input("Enter number of slices for person #" + str(personIndex) + ": "))
  
  if numOfSlices < 0:
    print("Not a valid entry, try again!\n")
  else:
    totalSlicesNeeded += numOfSlices
    personIndex += 1

# Calculate cost only if the amount of pizza ordered is more than 0
if totalSlicesNeeded > 0:
  wholePizzaNeeded = totalSlicesNeeded // SLICES_PER_PIZZA
  slizePizzaNeeded = totalSlicesNeeded % SLICES_PER_PIZZA
  totalCost = round(wholePizzaNeeded * costWholePizza + slizePizzaNeeded * costPerSlice, 2) 

remainingMoney = budget - totalCost

# Print outputs
if totalCost > budget:
  print("Your order cannot be completed.\nYou would need to purchase " + str(wholePizzaNeeded) + " pies and " + str(slizePizzaNeeded) + " slices")
else:
  print("You should purchase " + str(wholePizzaNeeded) + " pies and " + str(slizePizzaNeeded) + " slices")
  print("Your total cost will be: " + "{:.2f}".format(totalCost))

if remainingMoney == 0:
  print("You will have no money left after your order.")
elif remainingMoney < 0:
  print("This would put you over budget by " + "{:.2f}".format(remainingMoney * -1))
else:
  print("You will still have " + "{:.2f}".format(remainingMoney) + " left after your order")