# A farmer has a field , which is half in circle shape and rest rectangle.he needs to do fencing for entire field using barbed wire 5 times . circular section has radius 20m and rectangle length is 50m and breadth is 40m , if cost of barbed is 35rs/cm then calculate the total cost of fencing in field

radius = 20
length = 50
breadth = 40
cost_per_cm = 35

# Check values
if radius > 0 and length > 0 and breadth > 0:

    # Half circle perimeter
    # formula = pi * 2 + 2r
    half_circle = (3.14 * radius) + (2 * radius)

    # Rectangle perimeter
    #formula =  2(length + breadth)
    rectangle = 2 * (length + breadth)

    # Total boundary
    total_boundary = half_circle + rectangle

    # Fencing 5 times
    total_fencing = total_boundary * 5

    # Convert to cm
    total_fencing_cm = total_fencing * 100

    # Total cost
    total_cost = total_fencing_cm * cost_per_cm

    print("Total cost of fencing =", total_cost, "Rs")

else:
    print("Invalid dimensions")
