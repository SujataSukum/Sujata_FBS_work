# 10. Write a program to check if entered year is a leap year or not.

#type 1 : without passig parameter
        #   without return value

def leap_year():
    year = int(input("Enter the year: "))
    if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0) :
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')

leap_year()

#type 2 : with passig parameter
        #   without return value

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0) :
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')

year = int(input("Enter the year: "))
leap_year(year)

#type 3 : without passig parameter
        #   with return value

def leap_year():
    year = int(input("Enter the year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return year, True
    else:
        return year, False


year, res = leap_year()

if res:
    print(f"{year} is Leap Year")
else:
    print(f"{year} is Not a Leap Year")


# with passing parameter
# with return value
def leap_year(year):

    return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

year = int(input('Enter the year: '))

if leap_year(year):
    print(f'{year} is leap year.')
else:
    print(f'{year} is not leap year.')
