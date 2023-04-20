def sort_and_find(sequence: list) -> int:
    """
    Function which sort a list of numbers into a sequence and find the missing number if any
    :param sequence: a list of numbers in disorder
    :return: nothing if the sequence is complete, the missing number of the sequence
    """
    sequence.sort()
    x: int = int(sequence[0])

    for i in sequence:
        i: int = int(i)
        if i != x:
            return print(x)
        x = x + 1


def algo_missing(sequences_list: list) -> int:
    """
    Function which separate the two sequences into two list of numbers and gives out the response
    :param sequences_list: list with the two sequences
    :return: the missing number of one of the two sequences
    """
    r: list = []
    b: list = []
    for i in sequences_list:
        if i[-1] == "R":
            r.append(i[:-1])
        else:
            b.append(i[:-1])
    sort_and_find(r)
    sort_and_find(b)
