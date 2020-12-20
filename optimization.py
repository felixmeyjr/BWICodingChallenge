"""
Function file for optimization
"""


# Helper functions
def add_rel_value(products):
    """
    Calculates the relative values of products (value / weight)
    :param products: nested dict
    :return: updated product dict with relative value added
    """
    for key, value in products.items():
        products[key].update({'rel_value': value["benefit"] / value["weight"]})
    return products


def sort_dict(products):
    """
    Sorts the relative values of products dict in a descending order (largest to smallest)
    :param products: dict with hardware
    :return: sorted after rel value dict (descending)
    """
    return sorted(products.items(), key=lambda item: item[1]['rel_value'], reverse=True)


def load_truck(products, load_cap, driver_weight):
    """
    Puts items on trucks with highest value
    :param products:
    :param load_cap:
    :param driver_weight:
    :return: trucks: list with both truck loads
    """

    # Final solution list, each truck is stored in
    trucks = []

    # Iteration over both trucks (n_trucks = n_driver = len(driver_weight))
    for truck_num in range(len(driver_weight)):
        print("\nLoad truck No.", truck_num)

        # Initialize dict for storing all necessary values dependent of truck_num
        truck_load = {"total benefit": 0,
                      "weight capacity": load_cap,
                      "current weight": driver_weight[truck_num],
                      "driver weight": driver_weight[truck_num],
                      }

        # Iterate over all (sorted) products
        for key, value in products:
            if value["necc_units"] <= 0:
                print("No units of", key, "available.")
                continue

            # Calculate total load for one product
            load = value["necc_units"] * value["weight"]

            # Check if load of one product fits into total load capacity
            if truck_load["current weight"] + load <= load_cap:
                print("Fill all ", value["necc_units"], " units of ", key,  "in truck No. ", truck_num, "!", sep='')

                # Add new item to truck load todo rework this maybe
                truck_load.update({key: {"units": value["necc_units"],
                                         "benefit": value["benefit"] * value["necc_units"],
                                         "load_weight": load}})

                # Update total variables of truck load
                truck_load["current weight"] += load
                truck_load["total benefit"] += value["necc_units"] * value["benefit"]

                # Update warehouse
                value["necc_units"] = 0

            else:
                # Calculate maximum number of units that fit on truck
                max_units = (load_cap - truck_load["current weight"]) // value["weight"]

                if max_units >= 1:
                    print("Fill ", str(max_units), " units of ", key, " in truck No. ", truck_num, sep='')

                    # Add new item to truck load
                    truck_load.update({key: {"units": max_units,
                                             "benefit": value["benefit"] * max_units,
                                             "load_weight": max_units * value["weight"]}})

                    # Update total variables of truck load
                    truck_load["current weight"] += max_units * value["weight"]
                    truck_load["total benefit"] += max_units * value["benefit"]

                    # Update products accordingly
                    value["necc_units"] -= max_units
                else:
                    #print("No place for ", key, ".", sep='')
                    pass

        # Print process
        # print("Truck No.", truck_num, "total load:")
        # print(truck_load)
        # print_solution(truck_load, truck_num)

        # Add single truck to solution list
        trucks.append(truck_load.copy())
    return trucks


def print_solution(truck_load, truck_num):
    print("\nSolution for truck No.", truck_num)
    for key, value in truck_load.items():
        if type(value) == int:
            print(key, value)
        else:
            print(key)
            for key, value in value.items():
                print(key, value)
