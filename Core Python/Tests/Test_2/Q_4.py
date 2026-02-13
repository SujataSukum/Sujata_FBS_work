#WAp to calculate the total cost of painting ,the interior of building with four equal sized walls

height = float(input("Enter the length of wall in meters: "))

width = float(input("Enter the width of wall in meters: "))

cost_per_wall = float(input("Enter the cost per wall: "))

if height > 0 and width > 0 :
    area = (height  * width)
    Total_area = 4 * area
    Total_cost = Total_area * cost_per_wall

    print(f"Total cost of painting is {Total_cost} Rs.")

else:
    print("Inavlid inputs!")








