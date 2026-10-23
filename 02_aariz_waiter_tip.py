def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")



user_bill_amount = float(input("Please enter your bill amount: "))
tip_perc = float(input("Please enter your tip percentage: "))
total_calc(user_bill_amount, tip_perc)