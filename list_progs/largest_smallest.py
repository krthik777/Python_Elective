numbers = []
print("\nEnter numbers to add to the list. Press Enter without typing any number to stop.")
while True:
    try:
        value = int(input(">>> "))
    except ValueError:
        break
    numbers.append(value)

print("\nList:", numbers)
print("\nLargest Number:", max(numbers))
print("Smallest Number:", min(numbers))
