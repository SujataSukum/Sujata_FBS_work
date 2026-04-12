# 3. Python Program to Detect if Two Strings are Anagrams

str1 = input("Enter string 1: ")
str2 = input("ENter string 2: ")

str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2):
    print("String is Anagram")

else:
    print("String is not Anagram")
