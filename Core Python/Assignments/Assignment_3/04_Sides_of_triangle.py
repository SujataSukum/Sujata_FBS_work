#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

s1 = int(input("Enter the side 1 of Triangle: "))
s2 = int(input("Enter the side 2 of Triangle: "))
s3 = int(input("Enter the side 3 of Triangle: "))

if (s1+s2 > s3) and (s2+s3 > s1) and (s3+s1 > s2):
    print("Triangle is valid")

else:
    print("Triangle is not valid")

