# 6. Write a program to remove duplicates from the list.

list = [10,40,50,30,50,60,70,30,40,30,30]

unique = []

for i in list:
    if i not in unique:
        unique.append(i)

print(unique)

