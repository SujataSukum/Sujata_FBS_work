#7. Write a program to check if user has entered correct userid and password.

correct_userid = "root"
correct_password = "root123"

userid = input("Enter Userid: ")
password = input("Enter Password: ")

if(userid == correct_userid) and (password == correct_password):
    print("You entered Correct userid and password\n"
           "Login Sucessful!")

else:
    print("You entered Incorrect Userid and password\n"
    "Try Again!")

