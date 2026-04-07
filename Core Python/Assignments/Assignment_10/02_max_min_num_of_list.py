# 2. Write a program to find maximum and minimum element in a list.

list = [10,20,50,60,90]

max_num = list[0]
min_num = list[0]

for i in list:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i

print("Maximum element of the list",max_num)
print("Minimum element of the list",min_num)
