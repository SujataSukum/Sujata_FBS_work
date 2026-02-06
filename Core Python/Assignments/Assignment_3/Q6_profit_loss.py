#6. Write a program to calculate profit or loss.

cost_price = float(input("Enter cost price of product: "))
selling_price = float(input("Enter selling price of product: "))


if (selling_price > cost_price):
    profit = selling_price - cost_price
    print(f"You earned profit {profit} Rs")

elif (cost_price > selling_price):
    loss = cost_price - selling_price
    print("Loss: ",loss)

else:
    print("No profit , No loss")
