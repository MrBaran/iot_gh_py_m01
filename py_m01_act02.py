# Python Module 01: Activity 02
ghs = IoTGreenhouseService()

print("Fahrenheit to celsius converter")
print()
user_entry = input("Please enter degreee F to convert.")
degreeC = ghs.temperature.convert_F_to_C(user_entry)
print(degreeC)
