'''7. Write a program to solve the following series :
a. 1! + 2! + 3! + 4! + .....n!
'''

n = int(input("Enter the number till which you want factorial: "))
sum = 0

for i in range (1 , n+1): #runs from 1 to n
    fact = 1

    for j in range(1,i+1): # calculate factorial
        fact = fact * j

    sum = sum + fact

print("Sum of factorials are: ",sum)




