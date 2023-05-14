""" This python program solves the frequency challenge of the cortex game """


def algo_frequency(list_input: list):
    """
    This function allows you to meet the challenge of frequency
    :param list_input: List where you have to find the least repetitive element
    :return: The element found is returned as a string
    """
    dictionary: dict = {}
    for i in list_input:
        for j in i:
            dictionary[j] = dictionary.get(j, 0) + 1

    min_value = 10000000000000
    text_key: str = ""

    for key, value in dictionary.items():
        if value < min_value:
            min_value = value
            text_key = key

    return text_key

    """sorted_list = sorted(dictionary.items(), key=lambda x: x[1])

    return sorted_list[0][0]"""