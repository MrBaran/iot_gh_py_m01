''' IoT Greenhouse - Module 1: Activity 06
    Keith E. Kelly
    K2 Creatives, LLC
'''
#requires matplotlib install
#sudo apt-get install python3-matplotlib

from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService
import matplotlib.pyplot as plt
import numpy as np

ghs = IoTGreenhouseService()

l_readings = []
t_readings = []
print("Reading temperature and light levels.")
print("Press and hold push-button to end sampling.")
while ghs.switches.push_button.is_off():
    t_readings.append(ghs.temperature.get_outside_temp_F())
    l_readings.append(ghs.analog.light.get_value()/10)
    print(".", end="")
    sleep(.5)
    
print()
print("temp", t_readings)
print()
print("light",l_readings)
print()

x = np.arange(0, len(t_readings))
plt.plot(x, t_readings, label="temperature")
plt.plot(x, l_readings, label="light")
plt.legend()
plt.show()

