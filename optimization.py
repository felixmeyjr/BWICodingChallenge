

def sorted_relative_value(weights, values):
    """
    Calculates the value/ weight
    The higher the rel. value, the higher value per kg
    :param weights: weights dict
    :param values: values dict
    :return: sorted dict with relatives values
    """
    relative_values = {} # value/weight
    print(values["Notebook Büro 14"])
    print(weights["Notebook Büro 14"])

    print(values["Notebook Büro 14"]/weights["Notebook Büro 14"])

    # Get each rel. value
    for k in weights:
        relative_values[k] = values[k]/ weights[k]

    # Sort values in descending order
    relative_values = {k: v for k, v in sorted(relative_values.items(), key=lambda item: item[1], reverse=True)}

    return relative_values
