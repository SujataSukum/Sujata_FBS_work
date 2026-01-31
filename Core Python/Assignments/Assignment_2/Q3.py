# Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter the distance in feet:"))
inches = float(input("Enter the distance in inches:"))

meters = (feet * 30.48) + (inches * 2.54)
centimeters = (meters * 100)

print("The Distance in meters:",meters)
print("The Distance in centimeters",centimeters)


