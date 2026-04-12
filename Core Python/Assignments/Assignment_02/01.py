#1. Convert the time entered in hh,min and sec into seconds.

Hour = int(input("Enter the Hour:"))
Minutes = int(input("Enter the minutes:"))
Seconds = int(input("Enter the seconds:"))

Total_Seconds = (Hour * 3600) + (Minutes *  60) + 60

print("Total seconds are:",Total_Seconds)
