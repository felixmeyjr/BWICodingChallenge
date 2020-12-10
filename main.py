import numpy as np
import scipy

import optimization

"""
obj func = max(sum of value of hardware)

constraints: 

"""
"""
a) watch combination of driver

1. Calc all value/ weight ratio --> array with ratios
2. Sort array
3. Put in the transport car the item with highest value, repeat as long as cap is avail.
4. Repeat for 2nd car
notebook13[1] = weight
{notebook13 : {units: 205} , {weight: 2451}, {value: 40}}
notebook13[value] -> 40
"""


# Init values of task
# Weight of the driver; one driver per vehicle
weight_of_driver = [72.4, 85.7]

# Maximal capacity of one transport car
max_cap = 1100

# Needed hardware
# todo matrix/ numpy array?
hardware = np.array(["Notebook Büro 13", 205, 2451, 40], ["Notebook Büro 14", 420, 2978, 35],
                    ["Notebook outdoor", 450, 3625, 80], ["Mobiltelefon Büro", 60, 717, 30], [], [], [], [], [], [])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
