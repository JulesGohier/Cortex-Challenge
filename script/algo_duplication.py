""" This python program solves the duplicate challenge of the cortex game """


def algo_duplication(list_input: list):
    """
    This function allows you to meet the challenge of duplication
    :param list_input: List where you have to find the duplicates
    :return: The duplicate found is returned as a string
    """
    dictionary: dict = {}
    for i in list_input:
        for j in i:
            dictionary[j] = dictionary.get(j, 0) + 1

    for key, val in dictionary.items():
        if val == 2:
            return key
