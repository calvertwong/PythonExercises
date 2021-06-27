print("Valid Triangle Tester")

# Prompt user for point 1 coordinate
pointOneX = float(input("Enter Point #1 - x position:  "))
pointOneY = float(input("Enter Point #1 - y position:  "))

# Prompt user for point 2 coordinate
pointTwoX = float(input("Enter Point #2 - x position:  "))
pointTwoY = float(input("Enter Point #2 - y position:  "))

# Prompt user for point 3 coordinate
pointThreeX = float(input("Enter Point #3 - x position:  "))
pointThreeY = float(input("Enter Point #3 - y position:  "))

print("\nThe length of each side of your test shape is:\n")

# Calculate sides distance
sideOneDistance = round(((pointOneX - pointTwoX)**2 + (pointOneY -pointTwoY)**2)**0.5, 2)
sideTwoDistance = round(((pointOneX - pointThreeX)**2 + (pointOneY - pointThreeY)**2)**0.5, 2)
sideThreeDistance = round(((pointTwoX - pointThreeX)**2 + (pointTwoY - pointThreeY)**2)**0.5, 2)

# Print sides length
print("Side 1: " + "{:.2f}".format(sideOneDistance))
print("Side 2: " + "{:.2f}".format(sideTwoDistance))
print("Side 3: " + "{:.2f}".format(sideThreeDistance) + "\n")

# Check if the triangle is valid
if sideOneDistance + sideTwoDistance > sideThreeDistance and sideTwoDistance + sideThreeDistance > sideOneDistance and sideThreeDistance + sideOneDistance > sideTwoDistance:
  print("This is a valid triangle!")
  # Check the types of triangle
  if sideOneDistance == sideTwoDistance and sideTwoDistance == sideThreeDistance and sideThreeDistance == sideOneDistance:
    print("This is an equilateral triangle")
  elif sideOneDistance == sideTwoDistance or sideOneDistance == sideThreeDistance or sideTwoDistance == sideThreeDistance:
    print("This is an isosceles triangle") 
  else:
    print("This is a scalene triangle")
else:
  print("This is not a valid triangle")
 

