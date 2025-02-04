list1 = []
list2 = []

print("\nEnter numbers to add to the list. Press Enter without typing any number to stop.")
print("Input for List 1:")
while True:
    try:
        value = int(input(">>> "))
    except ValueError:
        break
    list1.append(value)

print("\nInput for List 2:")
while True:
    try:
        value = int(input(">>> "))
    except ValueError:
        break
    list2.append(value)

common_elements = []
for element in list1:
    if element in list2 and element not in common_elements:
        common_elements.append(element)

print("\nList 1:", list1)
print("List 2:", list2)
print("\nCommon Elements:", common_elements)
