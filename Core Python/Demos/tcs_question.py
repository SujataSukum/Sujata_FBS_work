loc = ['s1','s2','s3','s4','s5','s6']
dist = [1500,1800 , 2400,3400,2100,4000]

src = input("Enter source: ")
dest = input("Enter destination: ")

i_src = loc.index(src)
i_dest = loc.index(dest)

i= i_src
total_dist = 0

while(i!= i_dest):
    print(i)
    total_dist = total_dist + dist[i]
    if(i == len(loc) - 1 ):
        i = 0
    else:
        i += 1


print(total_dist)

cost_km = float(input("Enter cost per km: "))
cost = (total_dist/ 1000) * cost_km
print("Total_cost: ",cost)
