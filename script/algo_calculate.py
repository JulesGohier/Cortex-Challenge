def subset_sum(numbers: list, target: int, partial=[], partial_sum=0):
    """
    Function which returns a list of numbers (from the list *numbers*) which added together give the targeted number
    :param numbers: a list of 6 different numbers
    :param target: number targeted (central number)
    :param partial: a part of the original list *numbers*
    :param partial_sum: Sum of partial
    :return: a list of number which added together give the target number
    """
    if partial_sum == target:
        return partial
    if partial_sum > target:
        return None
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        solution = subset_sum(remaining, target, partial + [n], partial_sum + n)
        if solution is not None:
            return solution
    return None


def algo_calculate(numbers: list, target: int) -> str:
    """
    Function which returns all the different lists of numbers (from the list *numbers*)
    which added together give the targeted number into a string
    :param numbers: a list of 6 different numbers
    :param target: number targeted (central number)
    :return: string with a combination possible equal to the targeted number
    """
    result: str = "\""
    for number in subset_sum(numbers, target):
        n: str = str(number)
        result = result + n + "+"
    result = result[:-1] + "\""
    return result
