# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists


n = int(input("Enter number of elements: "))


list = []
for i in range(n):
    num = int(input("Enter element: "))
    list.append(num)
print(list)

even_list = []
odd_list = []

for i in list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("even list",even_list)
print("odd list",odd_list)

