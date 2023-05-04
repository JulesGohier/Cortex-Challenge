def search_start(matrix):
    """
    Find the coordinates of the starting point
    :param matrix: List[List[str]], labyrinth
    :return: Tuple[int, int], coordinates of the starting point "D"
    """
    for x, row in enumerate(matrix):
        if 'D' in row:
            y = row.index('D')
            return x, y


def valid_cell(matrix, x, y):
    """
    Check if the cell (x, y) is inside the matrix and isn't a wall
    :param matrix: List[List[str]], labyrinth
    :param x: x checked cell coordinate
    :param y: y checked cell coordinate
    :return: Boolean
    """
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] != "X"


def find_exit(matrix, start_point):
    """

    :param matrix: List[List[str]], labyrinth
    :param start_point: Tuple[int, int], coordinates of the starting point "D"
    :return:
    """
    stack = [start_point]
    visited = set()
    while stack:
        x, y = stack.pop()  # Take the last cell from the stack
        if matrix[x][y] in ('1', '2', '3', '4'):  # If we reach the exit, returns its coordinates
            return x, y
        visited.add((x, y))  # Otherwise, mark the cell as visited and add the boundary cells to the stack
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if valid_cell(matrix, nx, ny) and (nx, ny) not in visited:
                stack.append((nx, ny))
    return None  # In bug case, or if the card is wrong and there is no exit, return None


def algo_labyrinth(matrix: list):
    start_point: tuple = search_start(matrix)
    return find_exit(matrix, start_point)  # Start from the starting point
