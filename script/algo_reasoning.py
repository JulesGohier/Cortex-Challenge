def y_start(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'X':
                return j


def x_start(matrix, rows, cols):
    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] != 'X':
                return i


def y_end(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if matrix[i][j] != 'X':
                return j
    print("-1")


def x_end(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols-1, -1, -1):
        for i in range(rows-1, -1, -1):
            if matrix[i][j] != 'X':
                return i
    print("-1")


def compare_size(matrix1, matrix2, x0, y0):
    length1 = x_end(matrix1) - x0 + 1
    width1 = y_end(matrix1) - y0 + 1
    length2 = len(matrix2)
    width2 = len(matrix2[0])
    if length1 == length2 and width1 == width2:
        return True
    else:
        return False


def fits_in(matrix1, matrix2, x0, y0):
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    for i in range(rows2):
        for j in range(cols2):
            if matrix1[i + x0][j + y0] == matrix2[i][j]:
                return False
    return True


def algo_reasoning(matrix: list, piece: dict):
    rows = len(matrix)
    cols = len(matrix[0])
    x0 = x_start(matrix, rows, cols)
    y0 = y_start(matrix, rows, cols)

    if fits_in(matrix, piece["A"], x0, y0):
        if compare_size(matrix, piece["A"], x0, y0):
            return "A"
    if fits_in(matrix, piece["B"], x0, y0):
        if compare_size(matrix, piece["B"], x0, y0):
            return "B"
    if fits_in(matrix, piece["C"], x0, y0):
        if compare_size(matrix, piece["C"], x0, y0):
            return "C"
    else:
        return "None"
