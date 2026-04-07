# 2. Python Program to Merge Two Lists and Sort it

li1  = [10,20,30,50,60]
print(li1)

li2 = [23,56,78,90,11,43]
print(li2)

res = li1 + li2

print("Before sorting the list: ",res)

sort_list = res.sort(reverse=False)
print("After sorting the list: ",res)
