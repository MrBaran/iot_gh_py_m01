# Python Module 01: Activity 02
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

print("Fahrenheit to celsius converter")
print()
user_entry = input("Please enter degreee F to convert.")
degreeC = ghs.temperature.convert_F_to_C(user_entry)
print(degreeC)
#mod1
user_entry = input("Please enter degreee F to convert.")
degreeF = int(user_entry)
degreeC = ghs.temperature.convert_F_to_C(user_entry)
print(degreeC)
#mod2
user_entry = input("Please enter degreee F to convert.")
degreeF = float(user_entry)
degreeC = ghs.temperature.convert_F_to_C(user_entry)
print(degreeC)
#mod3
user_entry = input("Please enter degreee F to convert.")
if user_entry.isnumeric():
    degreeF = float(user_entry)
    degreeC = ghs.temperature.convert_F_to_C(user_entry)
    print(degreeC)
else:
    print("Sorry. I can't convert that value.")
#mod4
user_entry =""
while not user_entry.isnumeric():
    user_entry = input("Please enter degreee F to convert.")
degreeF = float(user_entry)
degreeC = ghs.temperature.convert_F_to_C(user_entry)
print(degreeC)
