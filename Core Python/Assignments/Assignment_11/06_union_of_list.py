# 6. Python Program to Find the Union of two Lists

li1 = [20,40,34,60,89]

li2 = [30,70,67,23,90]

union = li1.copy()

for i in li2:
    if i not in li1:
        union.append(i)

print(union)


