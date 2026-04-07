# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.


num = int(input("Enter the number which you want to check: "))

list = [10,40,50,30,50,60,70,30,40,30,30]
count = 0

for i in list:
    if i == num:
        count += 1

if count > 0:
    print(f'{num} is present in list for {count} times')

else:
    print(f'{num} is present in list')




