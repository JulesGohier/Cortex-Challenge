def algo_calculate(number_find: int, number_list: list):
    """
    A function that allows finding the addition sequence for the "number_find" bet the numbers of the sequence
    "number_list" (inspired by the backpack algorithm)
    :param number_find: Number to search
    :param number_list: List of start numbers
    :return: A string of characters where the numbers appear in ascending order and are separated by the + sign.
    """
    temporary_max_value = []
    temporary_combination = []

    for i in range(number_find + 1):
        temporary_max_value.append(0)
        temporary_combination.append([])

    for item in number_list:
        for w in range(number_find, item - 1, -1):
            if item + temporary_max_value[w - item] > temporary_max_value[w]:
                temporary_max_value[w] = item + temporary_max_value[w - item]
                temporary_combination[w] = temporary_combination[w - item] + [item]

    final_combination = temporary_combination[number_find]
    final_combination.sort()
    return '+'.join(str(elem) for elem in final_combination)