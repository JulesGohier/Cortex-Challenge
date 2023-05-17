""" This python program allows to solve the color challenge of the cortex game """


def compare_dictionary(dict1: dict, dict2: dict):
    """
    A function that compares two dictionaries and outputs the key of the element identical to the two dictionaries
    :param dict1: Dictionary to search
    :param dict2: Dictionary to compare
    :return: The key of the element identical to the two dictionaries
    """
    for key, value in dict1.items():
        if value == dict2[key]:
            return key


def algo_color(dictionary_input: dict):
    """
    This function allows you to solve the colour challenge
    :param dictionary_input: Dictionary where you have to look for
    :return: The word or key of the element that is identical in both dictionaries
    """
    dictionary_pattern: dict = {
        "argent": "silver",
        "beige": "beige",
        "blanc": "white",
        "bleu": "blue",
        "corail": "coral",
        "indigo": "indigo",
        "jaune": "yellow",
        "lavande": "lavender",
        "magenta": "magenta",
        "marron": "brown",
        "mauve": "purple",
        "noir": "black",
        "olive": "olive",
        "or": "gold",
        "orange": "orange",
        "orchidée": "orchid",
        "rose": "pink",
        "rouge": "red",
        "saumon": "salmon",
        "vert": "green",

        "silver": "silver",
        "white": "white",
        "blue": "blue",
        "coral": "coral",
        "yellow": "yellow",
        "lavender": "lavender",
        "brown": "brown",
        "purple": "purple",
        "black": "black",
        "gold": "gold",
        "orchid": "orchid",
        "pink": "pink",
        "red": "red",
        "salmon": "salmon",
        "green": "green",
    }

    return compare_dictionary(dictionary_input, dictionary_pattern)
