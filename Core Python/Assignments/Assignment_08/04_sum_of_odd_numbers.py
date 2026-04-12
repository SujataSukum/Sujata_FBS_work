# 4. Sum of all odd numbers between 1 to n

#type 1 : without passig parameter
        #   without return value
def sum_odd():
    n = int(input("Enter the value of n: "))
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum = sum + i

    print("Sum of the series is: ",sum)

sum_odd()

#type 2  : with passig parameter
        #   without return value

def sum_odd(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum = sum + i

    print("Sum of the series is: ",sum)

n = int(input("Enter the value of n: "))
sum_odd(n)

#type 3  : without passig parameter
        #   with return value

def sum_odd():
    n = int(input("Enter the value of n: "))
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum = sum + i

    return sum

res = sum_odd()
print("Sum of the series is: ",res)


#type 4  : with passig parameter
        #   with return value

def sum_odd(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum = sum + i
    return sum
   

n = int(input("Enter the value of n: "))
res = sum_odd(n)
print("Sum of the series is: ",res)
