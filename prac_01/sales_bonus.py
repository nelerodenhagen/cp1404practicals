"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
SMALL_DISCOUNT = 0.1
BIG_DISCOUNT = 0.15

sales = float(input('Enter sales: $'))
while sales >= 0:
    if sales < 1000:
        print(f"You get a ${(sales * SMALL_DISCOUNT):.2f} bonus")
    else:
        print(f"You get a ${(sales * BIG_DISCOUNT):.2f} bonus")
    sales = float(input("Enter sales: $ "))

