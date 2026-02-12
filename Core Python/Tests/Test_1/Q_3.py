# WAP to accept distance in km and convert it into meter and cm both

Distance = float(input("Enter Distance in Km: "))

# 1 km = 1000 m
# 1 m = 100 cm

meter = Distance * 1000
centimeter = meter * 100

print("Distance in meter: ",meter)
print("Distance in centimeter: ",centimeter)


