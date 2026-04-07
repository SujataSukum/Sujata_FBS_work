# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

li = [10,4,5,6,8,2]
print(li)
print(f"id of list {id(li)}")

new_list = li.copy()

print(new_list)
print(f"id of new_list {id(new_list)}")
