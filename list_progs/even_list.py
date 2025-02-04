numbers = []

print("\nEnter numbers to add to the list. Press Enter without typing any number to stop.")
while True:
    try:
        value = int(input(">>> "))
    except ValueError:
        break
    numbers.append(value)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
even_numbers.sort()

print("\nOriginal List:", numbers)
print("\nSorted Even Numbers:", even_numbers)
