#11. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

amount = int(input("Enter amount: "))

notes500 = amount // 500
amount = amount % 500

notes200 = amount // 200
amount = amount % 200

notes100 = amount // 100
amount = amount % 100

notes50 = amount // 50
amount = amount % 50

notes20 = amount // 20
amount = amount % 20

notes10 = amount // 10
amount = amount % 10

notes1 = amount

print("500 notes:", notes500)
print("200 notes:", notes200)
print("100 notes:", notes100)
print("50 notes:", notes50)
print("20 notes:", notes20)
print("10 notes:", notes10)
print("1 notes:", notes1)
