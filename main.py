## Title Print
print("Welcome to Sujal's Unit Converter")

## User input or either length category or weight category
cal = input("Which category would you like to convert? we support length(l) and Weight(w):  ")

## if statement, if the the input was the length
if cal == "l":
    unit1 = input("Which unit would you like to convert from: ")  # The starting unit input
    unit2 = input("Which unit would you like to convert to: ")  # The ending unit input
    num1 = input("Enter the value of the unit: ")  # The value of the input

    if unit1 == "cm" and unit2 == "m":  # cm to m
        ans = float(num1) / 100  # formula
        print(ans)
    elif unit1 == "mm" and unit2 == "cm":  # mm to cm
        ans = float(num1) / 10  # formula
        print(ans)
    elif unit1 == "m" and unit2 == "cm":  # m to cm
        ans = float(num1) * 100  # formula
        print(ans)
    elif unit1 == "cm" and unit2 == "mm":  # cm to mm
        ans = float(num1) * 10  # formula
        print(ans)
    elif unit1 == "mm" and unit2 == "m":  # mm to m
        ans = float(num1) / 1000  # formula
        print(ans)
    elif unit1 == "m" and unit2 == "mm":  # m to mm
        ans = float(num1) * 1000  # formula
        print(ans)
    elif unit1 == "km" and unit2 == "m":  # km to m
        ans = float(num1) * 1000  # formula
        print(ans)
    elif unit1 == "m" and unit2 == "km":  # m to km
        ans = float(num1) / 1000  # formula
        print(ans)
    elif unit1 == "mm" and unit2 == "km":  # mm to km
        ans = float(num1) / 1000000  # formula
        print(ans)
    else:
        print("Conversion not available yet")

if cal == "w":
    unit1 = input("Which unit would you like to convert from: ")
    unit2 = input("Which unit would you like to convert to: ")
    num1 = input("Enter the value of the unit: ")
    if unit1 == "kg" and unit2 == "lb":
        ans = float(num1) * 2.205
        print(ans)
    elif unit1 == "lb" and unit2 == "kg":
        ans = float(num1) / 2.205
        print(ans)
    elif unit1 == "oz" and unit2 == "g":
        ans = float(num1) * 28.35
        print(ans)
    elif unit1 == "g" and unit2 == "oz":
        ans = float(num1) / 28.35
        print(ans)
    elif unit1 == "kg" and unit2 == "g":
        ans = float(num1) * 1000
        print(ans)
    elif unit1 == "g" and unit2 == "kg":
        ans = float(num1) / 1000
        print(ans)
    elif unit1 == "lb" and unit2 == "g":
        ans = float(num1) * 454
        print(ans)
    elif unit1 == "g" and unit2 == "lb":
        ans = float(num1) / 454
        print(ans)
    elif unit1 == "oz" and unit2 == "lb":
        ans = float(num1) / 16
        print(ans)
    elif unit1 == "lb" and unit2 == "oz":
        ans = float(num1) * 16
        print(ans)
    else:
        print("Conversion not available yet")
