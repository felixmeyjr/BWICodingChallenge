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
# Weight of the driver; one driver per vehicle // unit: kg
weight_of_driverKG = [72.4, 85.7]
weight_of_driver = [72400, 85700]

# Maximal capacity of one transport car // unit: kg
max_capKG = 1100
max_cap = 1100000

# Needed hardware

# todo matrix/ numpy array?
# hardware = np.array(["Notebook Büro 13", 205, 2451, 40], ["Notebook Büro 14", 420, 2978, 35],
#                     ["Notebook outdoor", 450, 3625, 80], ["Mobiltelefon Büro", 60, 717, 30], [], [], [], [], [], [])

necc_units = {"Notebook Büro 13": 205, "Notebook Büro 14": 420, "Notebook outdoor": 450,
              "Mobiltelefon Büro": 60, "Mobiltelefon Outdoor": 157, "Mobiltelefon Heavy Duty": 220,
              "Tablet Büro klein": 620, "Tablet Büro groß": 250,
              "Tablet outdoor klein": 540, "Tablet outdoor groß": 370}

weights = {"Notebook Büro 13": 2451, "Notebook Büro 14" : 2978, "Notebook outdoor": 3625,
            "Mobiltelefon Büro": 717, "Mobiltelefon Outdoor": 988, "Mobiltelefon Heavy Duty": 1220,
            "Tablet Büro klein": 1405, "Tablet Büro groß": 1455,
            "Tablet outdoor klein": 1690, "Tablet outdoor groß": 1980}

values = {"Notebook Büro 13": 40, "Notebook Büro 14": 35, "Notebook outdoor": 80,
            "Mobiltelefon Büro": 30, "Mobiltelefon Outdoor": 60, "Mobiltelefon Heavy Duty": 65,
            "Tablet Büro klein": 40, "Tablet Büro groß": 40,
            "Tablet outdoor klein": 45, "Tablet outdoor groß": 68}


hardware = {"Notebook Büro 13": [205, 2451, 40], "Notebook Büro 14": [420, 2978, 35],
            "Notebook outdoor": [450, 3625, 80], "Mobiltelefon Büro": [60, 717, 30],
            "Mobiltelefon Outdoor": [157, 988, 60], "Mobiltelefon Heavy Duty": [220, 1220, 65],
            "Tablet Büro klein": [620, 1405, 40], "Tablet Büro groß": [250, 1455, 40],
            "Tablet outdoor klein": [540, 1690, 45], "Tablet outdoor groß": [370, 1980, 68]}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Get the relatives value (value/weight)
    rel_val = optimization.sorted_relative_value(weights, values)

    optimization.push_items_on_car(max_cap, weight_of_driver, rel_val, hardware)


    print(hardware["Notebook Büro 13"][0])
    print(type(hardware))  # prints hardware type (dict)
    print(hardware.keys())  # prints all hardware names
    #for key, list in hardware:  #todo funktioniert nicht, da value aus einer list besteht


    # Add the best rel values to the first transport car until the capacity is 100%
