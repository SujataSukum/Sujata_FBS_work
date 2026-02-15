#WAP  to accept year from user amd check if it is leap year or not

year = int(input("Enter the year: "))

if year % 4 == 0 :

    if year % 100 == 0:

        if year % 400 == 0:
            print(f"{year} is Leap year")

        else:
            print(f"{year} is Not a leap year")

    else:
        print(f"{year} is Leap year")


else:
    print(f"{year} is Not a leap year")





