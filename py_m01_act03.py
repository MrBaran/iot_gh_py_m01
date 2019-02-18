# Python Module 01: Activity 02
ghs = IoTGreenhouseService()

print("IoT Greenhouse - Python Module 01.")
print("User must activate keys to open greenhouse")
print()
key_num = 1
print("Activate Key", key_num)
while ghs.toggle.is_off():
    pass
for i in range(0, key_num):
    ghs.buzzer.beep()

#success - open greenhouse
ghs.servo.move(1)
