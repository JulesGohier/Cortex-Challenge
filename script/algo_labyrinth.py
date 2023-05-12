from collections import deque


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


def valid_cell(matrix, rows, cols, x, y):
    """
    Check if the cell (x, y) is inside the matrix and isn't a wall
    :param matrix: List[List[str]], labyrinth
    :param rows: number of rows in the matrix
    :param cols: number of cols in the matrix
    :param x: x checked cell coordinate
    :param y: y checked cell coordinate
    :return: Boolean
    """
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] != "X"


def algo_labyrinth(matrix):
    """
    Takes a matrix that represents a labyrinth and returns the coordinates of the exit by a depth-first search.
    The function enters into a while loop that continues until the stack is empty.
    Inside the loop, it pops the last cell from the stack and checks if it is the exit.
    If it is, it returns its coordinates.
    Otherwise, the cell is marked as visited and the boundary cells (top, bottom, left, right) are added to the stack,
    but only if they are valid cells and have not been visited yet.
    :param matrix: List[List[str]], labyrinth
    :return: the exit of the labyrinth
    """

    start_point: tuple = search_start(matrix)  # Coordinates of the starting point "D"
    stack = deque([start_point])
    visited = set()

    rows, cols = len(matrix), len(matrix[0])

    while stack:
        x, y = stack.pop()  # Take the last cell from the stack

        if matrix[x][y] in ('1', '2', '3', '4'):  # If we reach the exit, returns its coordinates
            return x, y
        visited.add((x, y))  # Otherwise, mark the cell as visited and add the boundary cells to the stack

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if valid_cell(matrix, rows, cols, nx, ny) and (nx, ny) not in visited:
                stack.append((nx, ny))

    return None  # In bug case, or if the card is wrong and there is no exit, return None
