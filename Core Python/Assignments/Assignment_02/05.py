#5. WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("Enter the cost price of book : "))
discount = int(input("Enter the discount percentage %: "))

discount_amt = (cost_price * discount) / 100
selling_price = cost_price - discount_amt

print(f"The selling price of book is {selling_price} Rs")
