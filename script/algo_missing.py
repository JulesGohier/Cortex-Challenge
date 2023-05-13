def search_missing(number_element: int, number_list: list):
    """
    Function to find a missing element in a sequence using an arithmetic equation
    :param number_element: Number of items in the list
    :param number_list: List containing the sequence
    :return: Return the missing element if it is in the sequence if not return false
    """
    arithmetic_sum = ((number_element + 1) * (number_list[0] + number_list[-1])) / 2
    sum_list = sum(number_list)
    missing_number = int(arithmetic_sum - sum_list)
    if missing_number not in number_list:
        return missing_number
    else:
        return False


def split_list(number_list: list, list1: list, list2: list):
    """
    Function to separate the numbers according to the color 'R' or 'B' into two distinct lists
    :param number_list: Number list with colors
    :param list1: Output list
    :param list2: Output list
    :return: Both lists completed
    """
    for element in number_list:
        if element[-1] == 'R':
            list1.append(int(element[:-1]))
        else:
            list2.append(int(element[:-1]))


def algo_missing(number_list: list):
    """
    This function allows to combine the two previous functions and to return the missing
    element of one of the two sequences
    :param number_list: Initial list
    :return: Missing element
    """
    listR: list = []
    listB: list = []
    split_list(number_list, listR, listB)
    listR.sort()
    listB.sort()

    nR = len(listR)
    nB = len(listB)

    if nR < nB:
        resultat = search_missing(nR, listR)
        if resultat:
            return resultat
        else:
            return search_missing(nB, listB)
    else:
        resultat = search_missing(nB, listB)
        if resultat:
            return resultat
        else:
            return search_missing(nR, listR)
