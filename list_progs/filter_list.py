numbers = []

print("\nEnter numbers to add to the list. Press Enter without typing any number to stop.")
while True:
    try:
        value = int(input(">>> "))
    except ValueError:
        break
    numbers.append(value)

max_value = int(input("Enter the maximum number: "))
filtered_list = list(filter(lambda x: x < max_value, numbers))

print("\nOriginal List:", numbers)
print("\nFiltered List:", filtered_list)
