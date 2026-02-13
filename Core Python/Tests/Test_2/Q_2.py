# WAP to accept three digit number . if first dgit is divisible of second digit and half of third digit then display "yes , you have done it" , otherwise display "please try real time"  e.g 428 , 214 etc


num = int(input("Enter three digit number: "))


third_num = num % 10
rem1 = num // 10


sec_num = rem1 % 10

first_num = rem1 // 10


if (first_num % sec_num == 0 ) and first_num == third_num // 2 :
    print("Yes you have done it")

else:
    print("please try real time")
