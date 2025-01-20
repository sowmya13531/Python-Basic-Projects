unit = input("Is this temperature in celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = ((9 * temp) / 5 + 32)
    print(f"The temperature in Fahrenheit is : {temp}'F")
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    print(f"The temperature in elsius is : {temp}'")
else:
    print(f"{unit} is an invalid unit of measurement")