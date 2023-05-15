def normal_reflect(y, x, light_direction):
    """
    Reflects the light beam when encountering a '/' mirror : change its direction and move by one cell
    :param y: y-coordinate of the current '/' cell
    :param x: x-coordinate of the current '/' cell
    :param light_direction: current light direction
    :return: new light direction
    """

    if light_direction == "North":
        light_direction = "East"
        x = x + 1
        return y, x, light_direction

    if light_direction == "South":
        light_direction = "West"
        x = x - 1
        return y, x, light_direction

    if light_direction == "West":
        light_direction = "South"
        y = y + 1
        return y, x, light_direction

    if light_direction == "East":
        light_direction = "North"
        y = y - 1
        return y, x, light_direction


def inverted_reflect(y, x, light_direction):
    """
    Reflects the light beam when encountering a '\\' mirror : change its direction and move by one cell
    :param y: y-coordinate of the current '\\' cell
    :param x: x-coordinate of the current '\\' cell
    :param light_direction: current light direction
    :return: new light direction
    """

    if light_direction == "North":
        light_direction = "West"
        x = x - 1
        return y, x, light_direction

    if light_direction == "South":
        light_direction = "East"
        x = x + 1
        return y, x, light_direction

    if light_direction == "West":
        light_direction = "North"
        y = y - 1
        return y, x, light_direction

    if light_direction == "East":
        light_direction = "South"
        y = y + 1
        return y, x, light_direction


def algo_reflection(matrix: list):
    """
    Simulate the travel of a light beam to solve the reflection problem
    :param matrix: map with a lamp (L)(=light beam start), numbers (1-15) and mirrors (/ and \\)
    :return: number reached by the light beam
    """
    y, x = 5, 2
    cell = matrix[y][x]
    light_direction = "North"
    result = ''
    while result == '':
        while cell in ('', "L"):

            if light_direction == "North":
                y = y - 1
                cell = matrix[y][x]

            elif light_direction == "South":
                y = y + 1
                cell = matrix[y][x]

            elif light_direction == "West":
                x = x - 1
                cell = matrix[y][x]

            elif light_direction == "East":
                x = x + 1
                cell = matrix[y][x]

        if cell == "/":
            y, x, light_direction = normal_reflect(y, x, light_direction)
            cell = matrix[y][x]

        elif cell == "\\":
            y, x, light_direction = inverted_reflect(y, x, light_direction)
            cell = matrix[y][x]

        else:
            result = matrix[y][x]

    return result
