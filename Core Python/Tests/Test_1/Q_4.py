# calculate the cost of painting the following building's wall (both interior and exterior) you need to accept area and cost of both interior and exterior

interior_area = float(input("Enter the area of interior wall: "))

exterior_area = float(input("Enter the area of exterior wall: "))

interior_rate = float(input("Enter the cost per unit area: "))
exterior_rate = float(input("Enter the cost per unit area: "))


interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate

Total_cost = interior_cost + exterior_cost

print("Interior wall painting cost: ",interior_cost)
print("Exterior wall painting cost: ",exterior_cost)
print("Total cost of painting: ",Total_cost)
