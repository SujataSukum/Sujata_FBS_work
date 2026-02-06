# gender = input("Enter gender (M/F): ")
# age = int(input("Enter Age: "))

# if gender == 'F':
#     if age > 17:
#         print("Eligible for marriage")
#     else:
#         print("Pehle PAdhai kar le")

# else:
#     if age > 21:
#         print("Eligible for marriage")

#     else:
#         print("Bada to ho ja")


# check person is eligble or not for voting

age = int(input("Enter age of person: "))

if age > 0 :
    if age > 17 and age < 111:
        print("Person is eligible for vote")

    else:
        print("Abhi bhai tereko time haii")

else:
        print("not eligible")
