# 11. Write a program to print all numbers which are divisible by m and n in the
# list.

li = [20,12,24,80,120,45,90]
res = []

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for i in li:
    if i % m == 0 and i % n == 0:
        res.append(i)
print(f"Elements which are divisible by {m} and {n} are {res}")

