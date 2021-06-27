# program header
print("\nPokemon Distance Calculator\n----------------------------------\n")

# Ask user for the name of first Pokemon
namePokemonOne = input("1. Enter name of first pokemon: ")

# Ask user for the name of second Pokemon
namePokemonTwo = input("2. Enter name of second pokemon: ")

# Ask user for the first Pokemon's X coordinate
xCoordPokemonOne = float(input("3. Enter x coordinate of first pokemon: "))

# Ask user for the first Pokemon's Y coordinate
yCoordPokemonOne = float(input("4. Enter y coordinate of first pokemon: "))

# Ask user for the second Pokemon's X coordinate
xCoordPokemonTwo = float(input("5. Enter x coordinate of second pokemon: "))

# Ask user for the second Pokemon's Y coordinate
yCoordPokemonTwo = float(input("6. Enter y coordinate of second pokemon: "))

# calculate distance between 2 points
computedDistance = ((xCoordPokemonTwo - xCoordPokemonOne)**2 + (yCoordPokemonTwo - yCoordPokemonOne)**2)**0.5

# print distance in inches with 2 decimals
print("\n\tThe distance between " + namePokemonOne + " and " + namePokemonTwo + " is " + "{:.2f}".format(computedDistance) + " inches.")