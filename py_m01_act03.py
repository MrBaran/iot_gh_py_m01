# Python Module 01: Activity 02
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

print("IoT Greenhouse - Python Module 01.")
print("User must activate keys to open greenhouse")
print("Position the potentiometer in the middle and set toggle switch to off.")
print()
#key 1
key_num = 1
print("Activate Key", key_num)
while ghs.switches.push_button.is_off():
    pass
for i in range(0, key_num):
    ghs.buzzer.beep()
    sleep(.5)
#key 2
key_num = 2
initial_pot_val = ghs.analog.pot.get_value()
new_pot_value = 0
print("Activate Key", key_num)
while new_pot_value <= initial_pot_val + 10:
    new_pot_value = ghs.analog.pot.get_value()
for i in range(0, key_num):
    ghs.buzzer.beep()
    sleep(.5)
#key 3 - TODO

#key 4 - TODO

#key 5 - TODO


#success - open greenhouse
print("Keys entered. Greenhouse open!")
ghs.servo.move(1)
