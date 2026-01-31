# 8 . Write a program to convert days into years, weeks and days.
# Start

# Input total number of days

# Calculate years
# years = days // 365    floor divsion gives whole value

# Find remaining days
# days = days % 365

# Calculate weeks
# weeks = days // 7

# Find remaining days
# days = days % 7

# Display years, weeks, and days

# Stop

day =  int(input("Enter the total days: "))

year = day // 360
remaining_days = day % 365

weeks = remaining_days // 7
days_left = remaining_days % 7

print(f"The Total time is {year} years , {weeks} week and {days_left} days")
