def get_dict_pair(ddict):
    dict_pairs = ddict.items()
    pair_iter = iter(dict_pairs)
    return next(pair_iter)


def sorted_relative_value(weights, values):
    """
    Calculates the value/ weight
    The higher the rel. value, the higher value per kg
    :param weights: weights dict
    :param values: values dict
    :return: sorted dict with relatives values
    """

    relative_values = {}  # value/weight

    # Get each rel. value
    for k in weights:
        relative_values[k] = values[k] / weights[k]

    # Sort values in descending order
    relative_values = {k: v for k, v in sorted(relative_values.items(), key=lambda item: item[1], reverse=True)}

    return relative_values


def push_items_on_car(load_cap, driver_weight, rel_values, hardware):
    """
    Puts the items with the highest value on the car, until no items are necc. anymore. Then take the item with the
    second highest rel. value. Repeat this with further items until the car is at full capacity
    :param load_cap: capacity of car
    :param driver_weight: array with weights of driver
    :param rel_values: sorted dict with relative values (values/ weight)
    :return: items on car todo as dict?
    """

    # Track current capacity
    curr_load = 0
    current_load = {}

    # Subtract the weight of driver from capacity todo remove driver from list afterwards
    load_cap -= min(driver_weight)

    # Repeat until capacity
    while curr_load <= load_cap:
        # Get highest relative value item i

        max_rel_val = get_dict_pair(rel_values)
        print(max_rel_val)

        # Update load dict with with necc. units of i


        # add weight of units i to current load (necc_units * weight)

        # Update all dicts by removing item i


def ys_add_rel_value(products):
    for key, value in products.items():
        products[key].update({'rel_value': value["value"] / value["weight"]})
    return products


def ys_sort_dict(products):
    return sorted(products.items(), key=lambda item: item[1]['rel_value'], reverse=True)


def ys_load_truck(products, load_cap, driver_weight):
    for truck_num in range(len(driver_weight)):
        print("\nLoad truck No.", truck_num)
        trucks = []
        truck_load = {"Total value": 0, "Weight capacity": load_cap, "actual weight": driver_weight[truck_num], "Driver weight": driver_weight[truck_num]}
        for key, value in products:
            if value["necc_units"] <= 0:
                print("No units of", key, "available.")
                continue
            load = value["necc_units"] * value["weight"]
            if truck_load["actual weight"] + load <= load_cap:
                print("Fill all ", value["necc_units"], " units of ", key,  "in truck No. ", truck_num, "!", sep='')
                truck_load.update({key: {"units": value["necc_units"], "value": value["value"] * value["necc_units"], "load_weight": load}})
                truck_load["actual weight"] += load
                truck_load["Total value"] += value["necc_units"] * value["value"]
                value["necc_units"] = 0  # Update warehouse
            else:
                max_units = (load_cap - truck_load["actual weight"]) // value["weight"]
                if max_units >= 1:
                    print("Fill ", str(max_units), " units of ", key, " in truck No. ", truck_num, sep='')
                    truck_load.update({key: {"units": max_units, "value": value["value"] * max_units, "load_weight": max_units * value["weight"]}})
                    truck_load["actual weight"] += max_units * value["weight"]
                    truck_load["Total value"] += max_units * value["value"]
                    value["necc_units"] -= max_units  # Update warehouse
                else:
                    #print("No place for ", key, ".", sep='')
                    pass
        print("Truck No.", truck_num, "total load:")
        print(truck_load)
        ys_print_solution(truck_load, truck_num)
        trucks.append(truck_load)  # funktioniert nicht
    return trucks


def ys_print_solution(truck_load, truck_num):
    print("\nSolution for truck No.", truck_num)
    for key, value in truck_load.items():
        if type(value) == int:
            print(key, value)
        else:
            print(key)
            for key, value in value.items():
                print(key, value)
