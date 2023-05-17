"""Optimisation du code --> utilisation de itertools plutot que extend """
from collections import Counter
import itertools


def frequency(card_list: list):
    """
    Function which groups all the words and their occurrence in a dict (cnt)
    The itertools.chain.from_iterable function chains the sublists into a single iterator.
    :param card_list: a list of lists which contains the words (game_data)
    :return: cnt, the dictionary referred to above
    """
    cnt: dict = Counter(itertools.chain.from_iterable(card_list))
    return cnt


def algo_duplication(card_list: list):
    """
    Function that return the duplicate element (an element which appears exactly 2 times) of a counter dict (cnt)
    :return: duplicate element
    """
    cnt: dict = frequency(card_list)
    for word, occurrence in cnt.items():
        if occurrence == 2:
            return word
