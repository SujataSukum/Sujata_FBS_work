# 8. Python Program to Remove the Characters of Odd Index Values in a
# String

s = input("Enter a string: ")

new_string = ""

for i in range(len(s)):
    if i % 2 == 0:
        new_string = new_string + s[i]

print("After renmoving odd index string is:", new_string)
