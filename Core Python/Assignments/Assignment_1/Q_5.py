# 5. Write a program to enter P, T, R and calculate Compound Interest.

p = int(input("Enter the principal amount: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate of interest: "))


com_amount = p * ( 1 + r/100)**t
compound_interest = com_amount - p

print("compound Interest is: ",compound_interest)
