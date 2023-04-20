def subset_sum(numbers: list, target: int, partial=[], partial_sum=0) -> list:
    """
    Function which returns a list of numbers (from the list *numbers*) which added together give the targeted number
    :param numbers: a list of 6 different numbers
    :param target: number targeted (central number)
    :param partial: a part of the original list *numbers*
    :param partial_sum: a part of the original list *numbers*
    :return: a list of number which added together give the target number
    """
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


def algo_calculation(numbers: list, target: int) -> str:
    """
    Function which returns all the different lists of numbers (from the list *numbers*)
    which added together give the targeted number into a string
    :param numbers: a list of 6 different numbers
    :param target: number targeted (central number)
    :return: string with all combinations possible equal to the targeted number
    """
    response: str = ""
    for subset in subset_sum(numbers, target):
        result: str = "\""
        for i in subset:
            x: str = str(i)
            result = result + x + "+"
        result = result[:-1] + "\""
        response = response + result + " OU "
    response = response[:-4]
    return response
