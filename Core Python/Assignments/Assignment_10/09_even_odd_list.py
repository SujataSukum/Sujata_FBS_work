# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
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



