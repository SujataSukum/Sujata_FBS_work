# 8 . Write a program to convert days into years, weeks and days.

day =  int(input("Enter the total days: "))

year = day // 360
remaining_days = day % 365

weeks = remaining_days // 7
days_left = remaining_days % 7

print(f"The Total time is {year} years , {weeks} week and {days_left} days")
