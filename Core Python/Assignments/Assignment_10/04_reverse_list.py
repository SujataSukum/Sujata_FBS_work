# 4. Write a program to reverse the list.

#using reverse method
li = [10,34,89,56,90]

li.reverse()

print("After reversing the list: ",li)


# using slicing

li [::-1]
print(li)


# using loop
rev = []
for i in li:
    rev += [i]

print("Reversed list: ",rev)

