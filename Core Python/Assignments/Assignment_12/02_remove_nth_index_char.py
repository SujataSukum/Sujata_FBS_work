# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String


s = input("Enter the string: ")

n = int(input("ENter the index number: "))

if n >= 0 and n < len(s):
    new_string = s[:n] + s[n+1:]
    print("New string:", new_string)
else:
    print("Invalid index")
