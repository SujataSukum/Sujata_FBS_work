# A man goes for shopping , he buys 5 products . accept the price of all products and display the total bill after adding 18% GST

p1_price = float(input("Enter the product 1 price: "))

p2_price = float(input("Enter the product 2 price: "))

p3_price = float(input("Enter the product 3 price: "))

p4_price = float(input("Enter the product 4 price: "))

p5_price = float(input("Enter the product 5 price: "))


if (p1_price > 0) and (p2_price > 0) and (p3_price > 0) and (p4_price > 0) and (p5_price > 0):
    Total_price = p1_price + p2_price + p3_price + p4_price + p5_price
    print("Total price of products: ",Total_price)

    gst = Total_price * 18/100
    print("GST(18%): ",gst)


    Total_bill = Total_price + gst
    print("Total Bill amount: ",Total_bill)

else:
    print("Invalid Input!")

