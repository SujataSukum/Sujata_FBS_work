# check string numbr using function

def strongNum(num):
    temp =num
    sum_fact = 0

    while num > 0:
        digit = num % 10
        fact = 1
        for i in range(1,digit +1):
            fact = fact * i
        sum_fact += fact
        num = num // 10


    if sum_fact == temp:
        return True

    else:
        return False


num = int(input("Enter the number: "))

if strongNum(num):
    print(f"{num} is strong number")

else:
    print(f"{num} is not strong number")







