def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

def algo_calculation(numbers, target):
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
