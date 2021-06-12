print("Welcome to Sujal's Unit Converter")
cal = input("Which category would you like to convert? we support length(l) and Weight(w):  ")

if cal == "l":
    unit1 = input("Which unit would you like to convert from: ")
    unit2 = input("Which unit would you like to convert to: ")
    num1 = input("Enter your value: ")

    if unit1 == "cm" and unit2 == "m":
        ans = float(num1) / 100
    elif unit1 == "mm" and unit2 == "cm":
        ans = float(num1) / 10
    elif unit1 == "m" and unit2 == "cm":
        ans = float(num1) * 100
    elif unit1 == "cm" and unit2 == "mm":
        ans = float(num1) * 10
    elif unit1 == "mm" and unit2 == "m":
        ans = float(num1) / 1000
    elif unit1 == "m" and unit2 == "mm":
        ans = float(num1) * 1000
    elif unit1 == "km" and unit2 == "m":
        ans = float(num1) * 1000
    elif unit1 == "m" and unit2 == "km":
        ans = float(num1) / 1000
    elif unit1 == "mm" and unit2 == "km":
        ans = float(num1) / 1000000


