# 10. Write a program to remove all occurrences of a given element in the list.

li = [10,40,50,30,50,60,70,30,40,30,30]

num = int(input("Enter Element: "))

new_list = []

for i in li:
    if i != num:
        new_list.append(i)
print(new_list)

