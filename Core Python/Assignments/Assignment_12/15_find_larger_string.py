# 15. Python Program to find larger string without using built-in functions.


str1 = input("Enter the string 1: ")

str2 = input("Enter the string 2: ")

count_str1 = 0
count_str2 = 0

for ch in str1:
    count_str1 += 1
print(f"Length of String1: ",count_str1)

for ch in str2:
    count_str2 += 1
print(f"Length of String2: ",count_str2)


if(count_str1 > count_str2):
    print(f'Larger String is:{str1}')

elif(count_str2 > count_str1):
    print(f'Larger String is:{str2}')

else:
    print(f"Both Strings are equal")

