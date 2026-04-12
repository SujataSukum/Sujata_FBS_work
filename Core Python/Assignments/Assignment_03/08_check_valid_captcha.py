# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
import random

correct_userid = "root"
correct_password = "root123"

userid = input("Enter Userid: ")
password = input("Enter Password: ")

if(userid == correct_userid) and (password == correct_password):
    print("You entered Correct userid and password!")


    # used to create random number between 1000 to 9999
    captcha = random.randint(1000,9999)
    print("Captcha: ",captcha)
    new_cap = int(input("Enter the Valid Captcha: "))

    if(captcha == new_cap):
        print("Login Successful!")

    else:
        print("Invalid Captcha,Try Again!")

else:
    print("You entered Incorrect Userid and password")
