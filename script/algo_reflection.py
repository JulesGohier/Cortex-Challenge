def more_near(value: int, list: list):
    """
    This function allows one to find the closest value to another one contained in a list and in a precise interval.
    :param value: Reference value
    :param list: List of values to test
    :return: Returns the value closest to the reference value
    """
    list_set = set(list)
    mini: float = float('inf')
    result: int = 0
    for num in list_set:
        diff = abs(num - value)
        if diff < mini:
            mini = diff
            result = num

    return result
def vertical_search(input_list: list, position: tuple, symbol: str, interval: tuple):
    """
    This function allows searching for mirrors in a column of the matrix
    :param input_list: List of existing mirrors in the matrix
    :param position: Current position in the matrix
    :param symbol: Current symbols
    :param interval: Search interval
    :return: Return the position of the new point and its symbol, a boolean to check if there is a mirror
    """
    mirror_find: list = []
    for i in input_list:
        if i[0][1] == position[1] and i[0] != position and interval[0] <= i[0][0] <= \
                interval[1]:
            mirror_find.append(i)

    mirror_find_length: int = len(mirror_find)
    if mirror_find_length >= 2:
        posx = more_near(position[0], [i[0][0] for i in mirror_find])
        if posx == None:
            return position, symbol, False
        for i in mirror_find:
            if i[0] == (posx, position[1]):
                symbol = i[1]
        return (posx, position[1]), symbol, True
    elif mirror_find_length == 1:
        for i in mirror_find:
            if i[0] == (mirror_find[0][0][0], position[1]):
                symbol = i[1]
        return (mirror_find[0][0][0], position[1]), symbol, True
    else:
        return position, symbol, False


def horizontal_search(input_list: list, position: tuple, symbol: str, interval: tuple):
    """
    This function allows searching for mirrors in a row of the matrix
    :param input_list: List of existing mirrors in the matrix
    :param position: Current position in the matrix
    :param symbol: Current symbols
    :param interval: Search interval
    :return: Return the position of the new point and its symbol, a boolean to check if there is a mirror
    """
    mirror_find: list = []

    for i in input_list:
        if i[0][0] == position[0] and i[0] != position and interval[0] <= i[0][1] <= \
                interval[1]:
            mirror_find.append(i)
    mirror_find_length: int = len(mirror_find)

    if mirror_find_length >= 2:
        posy = more_near(position[1], [i[0][1] for i in mirror_find])
        if posy == None:
            return position, symbol, False
        for i in mirror_find:
            if i[0] == (position[0], posy):
                symbol = i[1]
        return (position[0], posy), symbol, True
    elif mirror_find_length == 1:
        for i in mirror_find:
            if i[0] == (position[0], mirror_find[0][0][1]):
                symbol = i[1]
        return (position[0], mirror_find[0][0][1]), symbol, True
    else:
        return position, symbol, False


def algo_reflection(matrix: list):
    """
    This function combines the three previous functions to solve the reflection problem. By giving the possibility of reflection
    :param matrix : The matrix containing the mirror position
    :return : The number pointed by the mirror set
    """
    mirror_find_list: list = []
    symbol: list = ["/", "\\"]
    for row in range(1,5):
        for col in range(1,5):
            if matrix[row][col] in symbol:
                mirror_find_list.append(((row, col), matrix[row][col]))
    current_position: tuple = (5, 2)
    previous_position: tuple = (6, 0)
    current_symbol: str = "L"
    end: bool = True

    position_temporary = current_position
    current_position, current_symbol, end = vertical_search(mirror_find_list, current_position, current_symbol, (0, 5))
    if end:
        previous_position = position_temporary

    while end is not False:
        if (previous_position[0] < current_position[0] and current_symbol == "\\") or (previous_position[0] > current_position[0] and current_symbol == "/"):
            position_temporary = current_position
            current_position, current_symbol, end = horizontal_search(mirror_find_list, current_position, current_symbol,(current_position[1], 5))
            if end:
                previous_position = position_temporary
        elif (previous_position[0] < current_position[0] and current_symbol == "/") or (
                previous_position[0] > current_position[0] and current_symbol == "\\"):
            position_temporary = current_position
            current_position, current_symbol, end = horizontal_search(mirror_find_list, current_position, current_symbol,(0, current_position[1]))
            if end:
                previous_position = position_temporary
        elif (previous_position[1] > current_position[1] and current_symbol == "/") or (
                previous_position[1] < current_position[1] and current_symbol == "\\"):
            position_temporary = current_position
            current_position, current_symbol, end = vertical_search(mirror_find_list, current_position, current_symbol,(current_position[0], 5))
            if end:
                previous_position = position_temporary
        elif (previous_position[1] < current_position[1] and current_symbol == "/") or (
                previous_position[1] > current_position[1] and current_symbol == "\\"):
            position_temporary = current_position
            current_position, current_symbol, end = vertical_search(mirror_find_list, current_position, current_symbol,(0, current_position[0]))
            if end:
                previous_position = position_temporary

    if current_symbol == "L":
        return matrix[0][2]
    elif previous_position[1] > current_position[1]:
        if current_symbol == "/":
            return matrix[5][current_position[1]]
        elif current_symbol == "\\":
            return matrix[0][current_position[1]]

    elif previous_position[1] < current_position[1]:
        if current_symbol == "/":
            return matrix[0][current_position[1]]
        elif current_symbol == "\\":
            return matrix[5][current_position[1]]

    elif previous_position[0] < current_position[0]:
        if current_symbol == "/":
            return matrix[current_position[0]][0]
        elif current_symbol == "\\":
            return matrix[current_position[0]][5]

    elif previous_position[0] > current_position[0]:
        if current_symbol == "/":
            return matrix[current_position[0]][5]
        elif current_symbol == "\\":
            return matrix[current_position[0]][0]