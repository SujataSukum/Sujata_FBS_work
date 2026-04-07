# 3. Python Program to Sort the List According to the Second Element in Sublist

li = [[1,2],[4,3],[6,1],[7,4]]

li.sort(key=lambda x : x[1])


print("Sorted list: ",li)
