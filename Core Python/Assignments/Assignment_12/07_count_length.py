# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function

str = input("Enter the string: ")

count = 0

for ch in str:
    count += 1

print("Length of string is: ",count)
