#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a1 = int(input("Enter the Angle 1 of Triangle: "))
a2 = int(input("Enter the Angle 2 of Triangle: "))
a3 = int(input("Enter the Angle 3 of Triangle: "))

if (a1+a2+a3 == 180):
    print("Triangle is valid")

else:
    print("Triangle is not valid")
