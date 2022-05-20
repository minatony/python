import math
loan = int(input("Enter the loan principal:\n"))
word = input("""
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:\n
""")
if word == 'p':
    months = int(input("Enter the number of months:\n"))
    if loan % months == 0:
        print("Your monthly payment =", int(loan / months))
    else:
        print("Your monthly payment =", math.ceil(loan / months), "and the last payment =", loan - (months - 1) * math.ceil(loan / months))
if word == 'm':
    pay = int(input("Enter the monthly payment:\n"))
    result = math.ceil(loan / pay)
    if result == 1:
        print("It will take 1 month to repay the loan")
    else:
        print("It will take", result, "months to repay the loan")
"""
/////////////////////////////////////////////////////
"""
import math
word = input("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:\n
""")
if word == 'n':
    loan = int(input("Enter the loan principal:\n"))
    monthpay = int(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n"))
    base = 1 + interest / (12 * 100)
    n = math.ceil(math.log((monthpay / (monthpay - (base - 1) * loan)), base))
    if n // 12 == 0:
        print("It will take", math.ceil(n), "months to repay this loan!")
    elif n / 12 == 1:
        print("It will take 1 year to repay this loan!")
    else:
        print("It will take", n // 12, "years and", n - (n // 12) * 12, "months to repay this loan!")
if word == 'a':
    loan = int(input("Enter the loan principal:\n"))
    period = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    result = math.ceil(loan * interest / (12 * 100) * math.pow(1 + interest / (12 * 100), period)/(math.pow(1 + interest / (12 * 100), period) - 1))
    print(f'Your monthly payment = {result}!')
if word == 'p':
    annuity = float(input("Enter the annuity payment:\n"))
    period = int(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    result = math.floor(annuity / (interest / (12 * 100) * math.pow(1 + interest / (12 * 100), period) / (math.pow(1 + interest / (12 * 100), period) - 1)))
    print(f'Your loan principal = {result}!')
