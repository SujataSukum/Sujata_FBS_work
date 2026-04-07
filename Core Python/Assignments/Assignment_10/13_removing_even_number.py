# 13 . Write a program to print list after removing even numbers.

li = [10,3,4,56,77,90,33,65,1,3,2,67]
res_list=[]

for i in li:
    if i % 2 != 0:
        res_list.append(i)

print("After removing even numbers list is: ",res_list)

