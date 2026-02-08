#WAP to find the area & perimeter of following figure . (Accept the length,breadth , and radius from user.)

length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))
radius = float(input("Enter Radius: "))

pi = 3.14

#area of rectangle = l x b
# area of semicircle = 1/2 x pi x r x r

Total_area = (length * breadth) + (1/2 * pi * radius ** 2)
print("The Total area of this figure: ",Total_area)

#perimeter of rectangle = 2(l+ b)
#perimeter of semicircle = pi*r

Total_perimeter = (2*(length + breadth)) + (pi * radius)
print("The Total Perimeter of this figure: ",Total_perimeter)
