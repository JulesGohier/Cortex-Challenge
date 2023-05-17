def subset_sum(numbers: list, target: int, partial=[], partial_sum=0):
    """
    Recursively finds a list of numbers (from the list *numbers*) which added together give the targeted number
    :param numbers: a list of 6 different numbers
    :param target: number targeted (central number)
    :param partial: a part of the original list *numbers*
    :param partial_sum: Sum of partial
    :return: a list of number which added together give the target number
    """

    if partial_sum == target:  # If the partial sum equals the target sum, return the partial list as the solution
        return partial

    if partial_sum > target:  # If the partial sum exceeds the target sum, return None
        return None

    # Recursive case: enumerate over each element in the list, calculate the remaining numbers,
    # and recursively call the function on the remaining numbers with an updated partial list and partial_sum
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        solution = subset_sum(remaining, target, partial + [n], partial_sum + n)
        if solution is not None:
            return solution  # If a solution is found, return it

    return None  # If no solution is found, return None (should never happen)


def algo_calculate(target: int, numbers: list) -> str:
    """
    Function which returns a list of numbers (from the list *numbers*)
    which added together give the targeted number as a string
    :param target: number targeted (central number)
    :param numbers: a list of 6 different numbers
    :return: string with a combination possible equal to the targeted number
    """
    numbers.sort(reverse=True)  # Sort the numbers list in reverse order, generally faster in most cases.
    result: str = ""

    for number in subset_sum(numbers, target):  # Subset_sum finds the combination of numbers that add up to target
        n: str = str(number)
        result = result + n + "+"

    result = result[:-1]  # Remove the last "+" character from the string
    return result
