# Python Module 01: Activity 02
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

print("IoT Greenhouse - Python Module 01.")
print("User must activate keys to open greenhouse")
print("Be sure to position the potentiometer in the middle and the toggle switch to off.")
print()
key_num = 1
print("Activate Key", key_num)
while ghs.switches.push_button.is_off():
    pass
for i in range(0, key_num):
    ghs.buzzer.beep()

key_num = 2
initial_pot_val = ghs.analog.pot.get_value()
new_pot_value = 0
print("Activate Key", key_num)
while new_pot_value <= initial_pot_val + 10:
    new_pot_value = ghs.analog.pot.get_value()
for i in range(0, key_num):
    ghs.buzzer.beep()

key_num = 3
initial_light_val = ghs.analog.light.get_value()
new_light_value = 1024
print("Activate Key", key_num)
while new_light_value > initial_light_val - 100:
    new_light_value = ghs.analog.light.get_value()
for i in range(0, key_num):
    ghs.buzzer.beep()

key_num = 4
print("Activate Key", key_num)
while ghs.switches.toggle.is_off():
    pass
for i in range(0, key_num):
    ghs.buzzer.beep()

key_num = 5
current_temp = ghs.temperature.get_external_temp_C()
new_temp_value = 0
print("Activate Key", key_num)
while new_temp_value <= current_temp + 1:
    new_temp_value = ghs.temperature.get_external_temp_C()
for i in range(0, key_num):
    ghs.buzzer.beep()

#success - open greenhouse
print("Keys entered. Greenhouse open!")
ghs.servo.move(1)
