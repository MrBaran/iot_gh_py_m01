from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()
number = ghs.greenhouse.house_number

print("IoT Greenhouse - Python Introduction.")
print("House Number: " + number)
print()

print("Greenhouse controller")
print()

print("Turn potentiometer fully counter-clockwise.")
pot_value = ghs.analog.pot.get_value()
while pot_value > 0:
    pot_value = ghs.analog.pot.get_value()

current_temp = ghs.temperature.get_inside_temp_F()
print("Current internal temperature is " + str(current_temp))
print("Turn pot to set threshold temperature.")
print("Press push-button switch when done.")
TEMP_SPAN = 10
MAX_POT_VAL = 1023
old_threshold = current_temp
threshold = current_temp
while ghs.switches.push_button.is_off():
    pot_value = ghs.analog.pot.get_value()
    pot_percent = pot_value/MAX_POT_VAL
    delta_temp = TEMP_SPAN * pot_percent
    threshold = round(current_temp + delta_temp, 1)
    if threshold != old_threshold:
        print(threshold, end=" ")
        old_threshold = threshold
    sleep(.5)
print("\nThreshold temp set to " + str(threshold) + "\n")
print("Turn potentiometer fully counter-clockwise.")
while ghs.analog.pot.get_value() > 0:
    pass
print()
pos_index = 1
# Can you create code that uses the pot to set pos_index,
# an open position for the louver that is less than 1?
#--your extension here --

print()
#reset servo position
ghs.servo.move(0)
status = "CLOSED"
#monitoring temperature and updating louver
print("Monitoring...")
while True:
    tempF = ghs.temperature.get_inside_temp_F()
    print("temp = " + str(tempF))
    if tempF > threshold and status == "CLOSED":
        print("opening")
        ghs.servo.move(pos_index)
        status = "OPEN"
    elif tempF < threshold and status == "OPEN":
        print("closing")
        ghs.servo.move(0)
        status = "CLOSED"
    sleep(5)


