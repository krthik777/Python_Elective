binary_input = input("Enter a binary number: ")
decimal_value = 0
fractional_value = 0.0

if '.' in binary_input:
    integer_part, fractional_part = binary_input.split('.')
else:
    integer_part = binary_input
    fractional_part = ''

# Convert integer part ::
for index in range(len(integer_part)):
    digit = int(integer_part[index])
    power = len(integer_part) - index - 1
    decimal_value += digit * 2 ** power

# Convert the fractional part ::
for index in range(len(fractional_part)):
    digit = int(fractional_part[index])
    power = index + 1
    fractional_value += digit * 2 ** -power

# Combine both 
decimal_value += fractional_value
print(f"Decimal equivalent: {decimal_value}")
