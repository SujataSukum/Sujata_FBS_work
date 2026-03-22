# Write a program to calculate area of circle

#Type 1
def area_of_circle():
    radius = int(input("Enter the breadth: "))

    area = 3.14*radius*radius

    print(f"The area of rectangle is {area}")

area_of_circle()

#Type 2
def area_of_circle(radius):
    area = 3.14 * radius * radius

    print(f"The area of circle is {area}")


radius = int(input("Enter the radius: "))

area_of_circle(radius)

# Type 3
def area_of_circle():
    radius = int(input("Enter the radius: "))

    area = 3.14 * radius * radius
    return area

res = area_of_circle()
print(f"The area of rectangle is {res}")

# Type 4
def area_of_circle(radius):
    area = 3.14 * radius * radius

    return area

radius = int(input("Enter the radius: "))

res = area_of_circle(radius)

print(f"The area of circle is {res}")
