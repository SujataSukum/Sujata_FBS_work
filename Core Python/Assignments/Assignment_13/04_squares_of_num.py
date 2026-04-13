# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).


n = int(input("Enter value of n: "))

d = {}

# loop from 1 to n
for i in range(1, n + 1):
    d[i] = i * i

print("Result dictionary:", d)
