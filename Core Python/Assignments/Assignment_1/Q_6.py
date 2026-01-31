# 6. Write a Program to input two angles from user and find third angle of the triangle.

a1 = int(input("Enter the first angle of triangle: "))
a2 = int(input("Enter the second angle of traingle: "))

a3 = 180 - (a1  + a2)

print("The third angle of triangle is: ",a3)
