# 13. Python Program to count number of digits and letters in a string.

s = input("Enter a string: ")

letters = 0
digits = 0

for ch in s:
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letters += 1
    elif ch >= '0' and ch <= '9':
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
