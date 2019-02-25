# Python Module 01: Loop Example
from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

ghs = IoTGreenhouseService()

print("IoT Greenhouse - Python Module 01.")
print("Looping Example")
while ghs.switches.toggle.is_on():
    if ghs.analog.light.get_value() < 100:
        #It's night. Turn on the lights
        ghs.lamps.white.on()
    else:
        #It's day. Turn off the lights
        ghs.lamps.white.off()
    sleep(60)   #check every minute
    
