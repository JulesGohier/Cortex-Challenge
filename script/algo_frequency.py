"""Optimisation du code --> utilisation de itertools plutot que extend """
from collections import Counter
from itertools import chain


def least_common(cnt: Counter):
    """
    Function that returns the least common element of a counter dict (cnt)
    :param cnt: dict with words as keys and their occurrences as values
    :return: least common element of the counter dict
    """
    return min(cnt, key=cnt.get)


def algo_frequency(card_list: list):
    """
    Function which groups all the words and their occurrence in a dict (cnt) and returns its least common element
    :param card_list: a list of lists which contains the words (game_data)
    :return: the least common element
    """
    cnt: Counter = Counter(chain.from_iterable(card_list))
    return least_common(cnt)