''' IoT Greenhouse - Module 1: Activity 05
    Keith E. Kelly
    K2 Creatives, LLC

    Sets temperature setpoint using potentiometer and push-button
'''
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

print("IoT Greenhouse - Set Temperature Threshold")
print()

#check for pot in center position
pot_value = ghs.analog.pot.get_value()
if pot_value != 512:
    print("Please center potentiometer.")
    ghs.lamps.red.on()
while pot_value != 512:
    pot_value = ghs.analog.pot.get_value()
    sleep(.2)

#Pot good - start 
ghs.lamps.red.off()
current_temp = ghs.temperature.get_inside_temp_F()
print("Current internal temperature is", current_temp)
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
