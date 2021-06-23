## Title Print
print("Welcome to Sujal's Unit Converter")

## User input or either length category or weight category
cal = input("Which category would you like to convert? we support length(l) and Weight(w):  ")

## if statement, if the the input was the length
if cal == "l":
    unit1 = input("Which unit would you like to convert from: ")  ## The starting unit input
    unit2 = input("Which unit would you like to convert to: ")  ## The ending unit input
    num1 = input("Enter the value of the unit: ")  ## The value of the input

    if unit1 == "cm" and unit2 == "m":
        ans = float(num1) / 100
        print(ans)
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1) / 10
        print(ans)
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1) * 100
        print(ans)
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1) * 10
        print(ans)
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1) / 1000
        print(ans)
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1) * 1000
        print(ans)
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1) * 1000
        print(ans)
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1) / 1000
        print(ans)
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1) / 1000000
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
