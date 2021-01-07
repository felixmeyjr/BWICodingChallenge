from src import optimization

# Init values of task
# Weight of the driver; one driver per vehicle // unit: kg
weight_of_driverKG = [72.4, 85.7]
weight_of_driver = [72400, 85700]

# Maximal capacity of one transport car // unit: kg
max_capKG = 1100
max_cap = 1100000

# Needed hardware
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
