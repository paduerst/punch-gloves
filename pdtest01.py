# Gloves which know when you punch things.
# Hopefully can detect/distinguish different gestures.
# This script is for plotting the recorded values.
# Author: Peter Duerst
# Initialized: April 19, 2018
import time
import numpy as np

# Import the ADXL345 module and the plotting module.
import Adafruit_ADXL345
import matplotlib.pyplot as plt

# Create an ADXL345 instance.
# accel = Adafruit_ADXL345.ADXL345()

# Change the range.
# accel.set_range(Adafruit_ADXL345.ADXL345_RANGE_2_G)

# Change the data rate.
# accel.set_data_rate(Adafruit_ADXL345.ADXL345_DATARATE_100_HZ)

# print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
# while True:
#     # Read the X, Y, Z axis acceleration values and print them.
#     x, y, z = accel.read()
#     print('X={0}, Y={1}, Z={2}'.format(x, y, z))
#     # Wait half a second and repeat.
#     time.sleep(0.5)

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = 0.1*i
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()
