'''2. Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.'''

n = int(input("Enter the number of students: "))
total_percentage = 0

for i in range(1,n+1):
    print("\nStudent",i)

    total_marks = 0

    for j in range(1,6):
        marks = int(input("Enter marks of subject " + str(j) + ": "))
        total_marks = total_marks + marks


    percentage = (total_marks / j)

    print(f"Percentage of student{i} = {percentage} %")

    total_percentage = total_percentage + percentage

# After all students
average = total_percentage / n

print("\nAverage Percentage of all students =", average, "%")
