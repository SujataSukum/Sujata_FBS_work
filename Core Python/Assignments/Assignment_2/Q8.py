#8. Write a program to swap two numbers using third variable.

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the second number "))

print(f"Before swapping the value {num1}, {num2}")
temp = 0

temp = num1
num1 = num2
num2 = temp

print(f"after swapping the value {num1} , {num2}")
