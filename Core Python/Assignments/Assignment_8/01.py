#Write a program to calculate area of rectangle

#Type 1
def area_of_ractangle():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))

    area = length * breadth

    print(f"The area of rectangle is {area}")

area_of_ractangle()

#Type 2
def area_of_ractangle(length,breadth):
    area = length * breadth

    print(f"The area of rectangle is {area}")


length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
area_of_ractangle(length,breadth)

# Type 3
def area_of_ractangle():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))

    area = length * breadth
    return area

res = area_of_ractangle()
print(f"The area of rectangle is {res}")

# Type 4
def area_of_ractangle(length,breadth):
    area = length * breadth

    return area

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
res = area_of_ractangle(length,breadth)

print(f"The area of rectangle is {res}")
