def normal_turn(y, x, direction):

    if direction == "North":
        direction = "East"
        x = x + 1
        return y, x, direction

    if direction == "South":
        direction = "West"
        x = x - 1
        return y, x, direction

    if direction == "West":
        direction = "South"
        y = y + 1
        return y, x, direction

    if direction == "East":
        direction = "North"
        y = y - 1
        return y, x, direction


def inverted_turn(y, x, direction):

    if direction == "North":
        direction = "West"
        x = x - 1
        return y, x, direction

    if direction == "South":
        direction = "East"
        x = x + 1
        return y, x, direction

    if direction == "West":
        direction = "North"
        y = y - 1
        return y, x, direction

    if direction == "East":
        direction = "South"
        y = y + 1
        return y, x, direction


def algo_reflection(matrix: list):
    y, x = 5, 2
    cell = matrix[y][x]
    direction = "North"
    result = ''
    while result == '':
        while cell in ('', "L"):

            if direction == "North":
                y = y - 1
                cell = matrix[y][x]

            elif direction == "South":
                y = y + 1
                cell = matrix[y][x]

            elif direction == "West":
                x = x - 1
                cell = matrix[y][x]

            elif direction == "East":
                x = x + 1
                cell = matrix[y][x]

        if cell == "/":
            y, x, direction = normal_turn(y, x, direction)
            cell = matrix[y][x]

        elif cell == "\\":
            y, x, direction = inverted_turn(y, x, direction)
            cell = matrix[y][x]

        else:
            result = matrix[y][x]

    return result
