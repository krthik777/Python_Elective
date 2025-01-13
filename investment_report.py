initial_investment = float(input("Enter your initial investment amount (in INR): "))
annual_interest_rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the number of years you want to invest: "))

interest_rate = annual_interest_rate / 100
investment_value = initial_investment

print("\nInvestment Report:")
print("----------------------------")

for year in range(1, years + 1):
    investment_value += investment_value * interest_rate
    print("Year {}: ₹{:.2f}".format(year, investment_value))

final_amount = investment_value
growth = final_amount - initial_investment

print("----------------------------")
print("\nFinal Amount after {} years: ₹{:.2f}".format(years, final_amount))
print("Total Growth: ₹{:.2f}".format(growth))
