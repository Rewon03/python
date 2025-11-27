product = input("Enter Your product: ") #ASKING PRODUCT NAME AS INFO
rate = float(input("Enter rate of " + product + ":")) # ASKING RATE OF PRODUCT
QTY = int(input("Enter Quantity: ")) #ASKING QUANTITY OF PRODUCT
Discount = float(input("What would be discount %: ")) #ASKING WHAT WOULD BE DISCOUNT %

VAT= 0.13 #VAT IS ALWAYS 13% 
Total_Amount = rate * QTY 
discount_amount = Discount/100 * Total_Amount
Total_Amount_after_discount = Total_Amount - discount_amount
VAT_amount = 0.13 * Total_Amount_after_discount
Grand_total = Total_Amount_after_discount + VAT_amount

print("Hello Sir/Ma'am")
print("Product: ", product)
print("Rate: ", rate)
print("QTY: ", QTY)
print("Discount % : ", Discount)
print("Discount Amount: ", discount_amount)
print("VAT Amount: ", VAT_amount)
print("Grand total Amount after discount & VAT: ", Grand_total)
