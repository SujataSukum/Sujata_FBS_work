# 12. Write a program to create three lists of numbers, their squares and cubes

n =  int(input("Enter the number of elements: "))

li = []
for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)
print(li)

square_list = []
cube_list = []

for i in li:
    square_list.append(i ** 2)
    cube_list.append(i ** 3)

print("Square of the elements: ",square_list)
print("cube of elements are: ",cube_list)
