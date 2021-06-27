# original fluid volume in mL
fluidVolumeInMl = 250.0

# assign fluid common conversions values to variables
# if we were to use these numbers directly, there is a chance where we mistyped and in result of wrong converted values
mlToTsp = 0.202884
tbspToTsp = 3
cupToTbsp = 16
pintToCups = 2
quartToPints = 2
gallonToQuarts = 4
flozToMl = 29.5735

# conversion operations from mL to the respective units
convertedToTsp = fluidVolumeInMl * mlToTsp
convertedToTbsp = fluidVolumeInMl * mlToTsp / tbspToTsp
convertedToCups = convertedToTbsp / cupToTbsp
convertedToPint = convertedToCups / pintToCups
convertedToQuart = convertedToPint / quartToPints
convertedToGallon = convertedToQuart / gallonToQuarts
convertedToFloz = fluidVolumeInMl / flozToMl

# display results
print("------------------------------------------------------------------------------")
print("                 ml to US Fluid Volume Units")
print("------------------------------------------------------------------------------")

print("     mL:            ", fluidVolumeInMl)
print("     tsp:           ", convertedToTsp)
print("     tbsp:          ", convertedToTbsp)
print("     cups(s):       ", convertedToCups)
print("     pint(s):       ", convertedToPint)
print("     quart(s):      ", convertedToQuart)
print("     gallon(s):     ", convertedToGallon)
print("     fl oz:         ", convertedToFloz)