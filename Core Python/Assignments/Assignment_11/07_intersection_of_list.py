# 7. Python Program to Find the Intersection of Two Lists

li1 = [20,40,34,30,60,90]

li2 = [30,70,90,40,23,60]

intersection = []

for i in li1:
    if i in li2 and i not in intersection:
        intersection.append(i)
print(intersection)
