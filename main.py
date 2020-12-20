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
#weight_of_driver = [85700, 72400]

# Maximal capacity of one transport car // unit: kg
max_capKG = 1100
max_cap = 1100000

# Needed hardware


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

products = {"Notebook Büro 13": {"necc_units": 205, "weight": 2451, "benefit": 40},
            "Notebook Büro 14": {"necc_units": 420, "weight": 2978, "benefit": 35},
            "Notebook outdoor": {"necc_units": 450, "weight": 3625, "benefit": 80},
            "Mobiltelefon Büro": {"necc_units": 60, "weight": 717, "benefit": 30},
            "Mobiltelefon Outdoor": {"necc_units": 157, "weight": 988, "benefit": 60},
            "Mobiltelefon Heavy Duty": {"necc_units": 220, "weight": 1220, "benefit": 65},
            "Tablet Büro klein": {"necc_units": 620, "weight": 1405, "benefit": 40},
            "Tablet Büro groß": {"necc_units": 250, "weight": 1455, "benefit": 40},
            "Tablet outdoor klein": {"necc_units": 540, "weight": 1690, "benefit": 45},
            "Tablet outdoor groß": {"necc_units": 370, "weight": 1980, "benefit": 68}}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    products = optimization.add_rel_value(products)
    products = optimization.sort_dict(products)
    truck_load = optimization.load_truck(products, max_cap, weight_of_driver)
    #print(truck_load)
"""
Solution:
Truck No. 0:
{'Total value': 44764, 'Weight capacity': 1100000, 'actual weight': 1099276,
'Driver weight': 72400,
'Mobiltelefon Outdoor': {'units': 157, 'value': 9420, 'load_weight': 155116},
'Mobiltelefon Heavy Duty': {'units': 220, 'value': 14300, 'load_weight': 268400},
'Mobiltelefon Büro': {'units': 60, 'value': 1800, 'load_weight': 43020},
'Tablet outdoor groß': {'units': 283, 'value': 19244, 'load_weight': 560340}}

Truck No. 1:
{'Total value': 29876, 'Weight capacity': 1100000, 'actual weight': 1099555,
'Driver weight': 85700,
'Tablet outdoor groß': {'units': 87, 'value': 5916, 'load_weight': 172260},
'Tablet Büro klein': {'units': 599, 'value': 23960, 'load_weight': 841595}}

Total value: 74640
(Bei Fahrertausch total value von 74600)
"""
    # Get the relatives value (value/weight)
    # rel_val = optimization.sorted_relative_value(weights, values)

    # optimization.push_items_on_car(max_cap, weight_of_driver, rel_val, hardware)

    # Add the best rel values to the first transport car until the capacity is 100%
