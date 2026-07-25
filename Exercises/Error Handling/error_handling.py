

#For practicing error handling in python

while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Please enter a valid age.")
    else:
        print(f"Next year you will be: {age + 1}")
        break

while True:
    try:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
    except ValueError:
        print("Please enter a valid number.")
    else:
        print(f"Sum: {num1 + num2}")
        print(f"Difference: {num1 - num2}")
        print(f"Product: {num1 * num2}")
        break

filename = input("Please enter a filename: ")

if filename == "":
    print("Filename cannot be empty.")
else:
    print(f"Processing file...")