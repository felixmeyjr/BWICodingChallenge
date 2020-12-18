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



import numpy as np


# import gurobipy as gp # todo @yannik ich kann kein Gurobi ausführen. Hab keine Lizenz
# from gurobipy import GRB
#
# def gurobi_solver():
#     try:
#
#         # Create model
#         m = gp.Model("LIP")
#
#         # Create variables
#
#         # Objective function
#
#         # Constraints
#
#         # Optimization
#         m.optimize()
#
#     # Error handling
#     except gp.GurobiError as e:
#         print('Error code ' + str(e.errno) + ": " + str(e))
#
#     except AttributeError:
#         print('Encountered an attribute error')
