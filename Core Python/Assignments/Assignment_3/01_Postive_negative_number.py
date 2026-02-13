#1. Write a program to check if the given number is positive or negative.

num = int(input("Enter the number: "))

if num > 0 :
    print(f"{num} is Positive Number")

elif num == 0 :
    print(f"{num} is Neutral")

else:
    print(f"{num} is Negative Number")
