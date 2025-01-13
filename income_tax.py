print("-------------------------\nIncome Tax Estimator\n-------------------------")
total_income = int(input("Enter your total income:"))
total_deductions = int(input("Enter your deductions:"))

net_income = total_income - total_deductions


print("\nNet Taxable Income: ", net_income)

# Initialize excess_income
excess_income = 0

if net_income <= 300000:
    tax_due = 0
    tax_rate = 0
elif 300000 < net_income <= 700000:
    excess_income = net_income - 300000
    tax_due = 0
    tax_rate = 0.05
elif 700000 < net_income <= 1000000:
    excess_income = net_income - 700000
    tax_due = 20000
    tax_rate = 0.1
elif 1000000 < net_income <= 1200000:
    excess_income = net_income - 1000000
    tax_due = 50000
    tax_rate = 0.15
elif 1200000 < net_income <= 1500000:
    excess_income = net_income - 1200000
    tax_due = 80000
    tax_rate = 0.2
else:
    excess_income = net_income - 1500000
    tax_due = 140000
    tax_rate = 0.3

total_tax = tax_due + (excess_income * tax_rate)

print("-----------------------------------------\n| Total tax payable is:","{:.3f}".format(total_tax),"INR |\n-----------------------------------------")
