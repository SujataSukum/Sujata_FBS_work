# 10. Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = input("Enter gender (M/F): ")
age = int(input("Enter Age: "))

if gender == 'F':
    if age > 17:
        print("Eligible for marriage")
    else:
        print("Pehle PAdhai kar le")

else:
    if age > 21:
        print("Eligible for marriage")

    else:
        print("Bada to ho ja")
