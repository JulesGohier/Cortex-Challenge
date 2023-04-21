"""Maybe import algo_frequency instead of rewrite all the functions"""
from collections import Counter


def extend_list(list_of_lists: list) -> list:
    """
    Function that concatenate a list of lists into a unique list
    :param list_of_lists: it's pretty explicit, isn't it?
    :return: a list with all the value of all the precedent lists
    """
    unique_list: list = []
    for sublist in list_of_lists:
        unique_list.extend(sublist)
    return unique_list


def frequency(card_list: list):
    cnt = Counter()
    complete_list = extend_list(card_list)
    for word in complete_list:
        cnt[word] += 1
    return cnt


def algo_duplication(card_list: list):
    """
    Function that return the duplicate element  of a counter list (cnt)
    :return: least_common element
    """
    cnt = frequency(card_list)
    for animal, occurence in cnt.items():
        if occurence == 2:
            return print(animal)
