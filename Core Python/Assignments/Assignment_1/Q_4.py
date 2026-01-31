#4. Write a program to enter P, T, R and calculate simple Interest.

p = int(input("Enter the principal amount: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate of interest: "))


simple_ineterest = p*t*r / 100

print("Simple Interest is: ",simple_ineterest)
