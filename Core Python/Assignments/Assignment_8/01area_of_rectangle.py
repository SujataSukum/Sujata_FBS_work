#Write a program to calculate area of rectangle

#type 1 : without passig parameter
        #   without return value
def area_of_ractangle():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))

    area = length * breadth

    print(f"The area of rectangle is {area}")

area_of_ractangle()

#type 2 : with passig parameter
        #   without return value
def area_of_ractangle(length,breadth):
    area = length * breadth

    print(f"The area of rectangle is {area}")


length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
area_of_ractangle(length,breadth)

#type 3 : without passig parameter
        #   with return value

def area_of_ractangle():
    length = int(input("Enter the length: "))
    breadth = int(input("Enter the breadth: "))

    area = length * breadth
    return area

res = area_of_ractangle()
print(f"The area of rectangle is {res}")

#type 4 : with passig parameter
        #   with return value
def area_of_ractangle(length,breadth):
    area = length * breadth

    return area

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
res = area_of_ractangle(length,breadth)

print(f"The area of rectangle is {res}")
