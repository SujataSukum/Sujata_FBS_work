# 3. Write a program to find the second largest element in the list.

li = [10, 40, 60, 30, 70, 100]

max_val = li[0]
sec_max = li[0]

for i in li:
    if i > max_val:
        sec_max = max_val
        max_val = i
    elif i > sec_max and i != max_val:
        sec_max = i

print("Second max value is:", sec_max)
