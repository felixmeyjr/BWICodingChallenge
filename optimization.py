

def sorted_relative_value(weights, values):
    """
    Calculates the value/ weight
    The higher the rel. value, the higher value per kg
    :param weights: weights dict
    :param values: values dict
    :return: sorted dict with relatives values
    """

    relative_values = {} # value/weight
    # print(values["Notebook Büro 14"])
    # print(weights["Notebook Büro 14"])
    #
    # print(values["Notebook Büro 14"]/weights["Notebook Büro 14"])

    # Get each rel. value
    for k in weights:
        relative_values[k] = values[k]/ weights[k]

    # Sort values in descending order
    relative_values = {k: v for k, v in sorted(relative_values.items(), key=lambda item: item[1], reverse=True)}

    return relative_values

def push_items_on_car(load_cap, driver_weight, rel_values, necc_units, weights, values):
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
    current_load = {} # {"telefon" :

    # backup
    bRelvalues = rel_values
    bNeccunits = necc_units
    bWeights = weights
    bValues = values

    # Repeat until capacity
    while curr_load <= load_cap:
        # Get highest relative value item i

        # Update load dict with with necc. units of i

        # add weight of units i to current load (necc_units * weight)

        # Update all dicts by removing item i
        pass






