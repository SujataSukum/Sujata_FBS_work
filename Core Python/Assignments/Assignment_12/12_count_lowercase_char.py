# 12. Python Program to count number of lowercase characters in a string.

str = input("Enter the string: ")

count = 0

for ch in str:
    if ch >= 'a' and ch <= 'z':
        count += 1

print("lower char are:",count)
