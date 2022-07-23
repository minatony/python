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
"""
///////////////////////////////////////////////////////////////
"""
import argparse
import math

creditcalc = argparse.ArgumentParser(description="This programs prints monthly payment amount")
creditcalc.add_argument("-p1", "--type", choices=["annuity", "diff"], help="Incorrect parameters")
creditcalc.add_argument("-p2", "--payment")
creditcalc.add_argument("-p3", "--principal")
creditcalc.add_argument("-p4", "--periods")
creditcalc.add_argument("-p5", "--interest")
args = creditcalc.parse_args()
check = [args.type, args.payment, args.principal, args.periods, args.interest]
count = 0
for x in check:
    if x is None:
        count += 1
if count > 1:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif args.type == "annuity":
    i = float(args.interest) / 1200
    if args.principal is None:
        p = math.floor(int(args.payment)
                       * (math.pow(i + 1, int(args.periods)) - 1) / (i * math.pow(1 + i, int(args.periods))))
        c = int(args.payment) * int(args.periods) - p
        print(f"Your loan principal = {p}!\nOverpayment = {c}")
    elif args.payment is None:
        a = math.ceil((int(args.principal) * i
                       * math.pow(1 + i, int(args.periods))) / (math.pow(1 + i, int(args.periods)) - 1))
        c = a * int(args.periods) - int(args.principal)
        print(f"Your annuity payment = {a}!\nOverpayment = {c}")
    elif args.periods is None:
        pe = math.ceil(math.log(int(args.payment) / (int(args.payment) - i * int(args.principal)), 1 + i))
        if pe // 12 == 0:
            print(f"It will take {pe} months to repay this loan!")
        elif pe / 12 == 1:
            print("It will take 1 year to repay this loan!")
        else:
            print(f"It will take {pe // 12} years and {pe - (pe // 12) * 12} months to repay this loan!")
        c = int(args.payment) * pe - int(args.principal)
        print(f"Overpayment = {c}")
elif args.type == "diff":
    b = 0
    i = float(args.interest) / 1200
    for count in range(int(args.periods)):
        a = math.ceil(int(args.principal) / int(args.periods)
                      + i * (int(args.principal) - int(args.principal) * (count - 1) / int(args.periods)))
        print(f"Month {count}: payment is {a}")
        b += a
    c = b - int(args.principal)
    print(f"Overpayment = {c}")
