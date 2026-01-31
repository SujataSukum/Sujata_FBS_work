#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

maths = int(input("Enter the marks of maths: "))
english =int(input("Enter the marks of English: "))
science = int(input("Enter the marks of science: "))
history = int(input("Enter the marks of history: "))
economics = int(input("Enter the marks of economics: "))


total_marks = maths + english + science + history + economics

percentage = (total_marks/5) 
print(percentage)
