
#7. Program to Find the Roots of a Quadratic Equation

# Start

# Input values of a, b, and c

# Calculate the discriminant
# D = b² − 4ac

# If D > 0

# Calculate two real roots
# root1 = (-b + D ** 0.5) / (2a)
# root2 = (-b − D ** 0.5) / (2a)

# Else if D = 0

# Calculate one real root
# root = -b / (2a)

# Else

# Display No real roots

# Display the roots

# Stop


a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = b*b - 4*a*c
if d > 0:
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("Two roots are:", root1, "and", root2)

elif d == 0:
    root = -b / (2*a)
    print("One real root is:", root)

else:
    print("No real roots")
