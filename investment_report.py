principal = float(input("Enter the initial investment amount: "))
rate_of_interest = float(input("Enter the annual interest rate (in percentage): "))
investment_period = int(input("Enter the number of years: "))

starting_amount = principal
total_amount = principal
rate_of_interest /= 100

print("Year\tStarting_Amount\tInterest\tTotal_Amount")
for year in range(1, investment_period + 1):
    yearly_interest = round(rate_of_interest * starting_amount, 2)
    total_amount += yearly_interest
    print(f"{year}\t{starting_amount:.2f}\t\t{yearly_interest:.2f}\t\t{total_amount:.2f}")
    starting_amount = total_amount

print()
print(f"The total amount after {investment_period} years is ₹{total_amount:.2f}")
print(f"The total interest earned over {investment_period} years is ₹{total_amount - principal:.2f}")
