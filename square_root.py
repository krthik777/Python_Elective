number = float(input("Enter a number: "))

if number < 0:
    print("Please enter a positive number.")
else:
    approximation = number / 2.0
    tolerance = 0.0000001
    while True:
        updated_value = (approximation + number / approximation) / 2.0
        if abs(approximation - updated_value) < tolerance:
            print(f"Square root of {number} is approximately {updated_value}")
            break
        approximation = updated_value
