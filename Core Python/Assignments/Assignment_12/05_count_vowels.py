# 5. Python Program to Count the Number of Vowels in a String

s = input("Enter the string: ")
count = 0

for i in s:
    if i in 'aeiouAEIOU':
        count += 1

print("Total vowels are: ",count)



