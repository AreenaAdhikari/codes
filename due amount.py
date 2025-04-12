
bill_amount = float(input("Enter the total bill amount: €"))

amount_paid = float(input("Enter the amount paid by the customer: €"))

if amount_paid < bill_amount:
    due_amount = bill_amount - amount_paid
    print(f"Customer still owes €{due_amount:.2f}")
elif amount_paid > bill_amount:
    change = amount_paid - bill_amount
    print(f"Customer has overpaid. Return €{change:.2f} as change")
else:
    print("Bill fully paid. No due amount.")