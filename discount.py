#program to compute discount
total_amount  =float(input ("Enter the amount purchased:"))
if total_amount > 1000:
    discount = 0.05*total_amount
    discounted_amount = total_amount - discount
    print("The discount is", discount)
    print("The price after discount is:",discounted_amount)
else:
    print("No discount!!")