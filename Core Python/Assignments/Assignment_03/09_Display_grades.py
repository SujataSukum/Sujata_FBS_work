# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

maths = int(input("Enter the marks of maths: "))
english =int(input("Enter the marks of English: "))
science = int(input("Enter the marks of science: "))
history = int(input("Enter the marks of history: "))
economics = int(input("Enter the marks of economics: "))

total_marks = maths + english + science + history + economics

percentage = (total_marks/500) * 100

print("Total Marks: ",total_marks)
print(f"Percentage: {percentage}%")

if(percentage >= 75):
    print("Grade:First Class with Distinction")

elif(percentage >= 60):
    print("Grade:First Class")

elif(percentage >= 50):
    print("Grade:Second Class")

elif percentage >= 40:
    print("Grade:Pass")

else:
    print("Grade:Fail")

