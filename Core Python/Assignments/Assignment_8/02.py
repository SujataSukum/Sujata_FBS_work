# Write a program to calculate area of circle

#Type 1
def area_of_circle():
    radius = int(input("Enter the breadth: "))

    area = 3.14*radius*radius

    print(f"The area of rectangle is {area}")

area_of_circle()

#Type 2
def area_of_ractangle(radius):
    area = 3.14 * radius * radius

    print(f"The area of rectangle is {area}")


radius = int(input("Enter the length: "))

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
