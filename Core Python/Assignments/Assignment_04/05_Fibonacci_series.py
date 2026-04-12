# 5. WAP to print Fibonacci series upto n.

num = int(input("Enter the number: "))

a = -1
b = 1
c = 0

while(c<num):
    c = a+b
    print(c,end = ' ')
    a = b
    b = c
