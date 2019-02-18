# Python Module 01: Activity 02
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

print("Fahrenheit to Celsius converter")
print()
user_entry = input("Please enter degreee F to convert.")
degreeC = ghs.temperature.convert_F_to_C(user_entry)
print(degreeC)
