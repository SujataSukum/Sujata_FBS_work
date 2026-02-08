num = int(input("Enter the number: "))

temp = num

while(temp > 0):
    d = temp % 10    #to seperate out the digit
    print(d)
    temp //= 10
