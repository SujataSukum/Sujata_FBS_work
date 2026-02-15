# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passengers = int(input("Enter the number of passengers: "))

cost =  float(input("Enter the per ticket cost: "))

total_amount = 0

for i in range(1,passengers+1):
    print("\nPassenger",i)

    age = int(input("Enter the age: "))

    if(age < 12):
        discount = cost * 0.30
        final_cost = cost - discount
        print("child discount applied")


    elif(age > 59):
        discount = cost * 0.50
        final_cost = cost - discount
        print("senior citizen discount applied")


    else:
        final_cost = cost
        print("no discount applied")

    print(f"Total cost per passenger {i} = {final_cost}")

    total_amount += final_cost


print("\nTotal amount of tickets to be paid: ",total_amount)
