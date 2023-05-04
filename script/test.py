"drawing": [
    ["X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "", "", "X", "X", "X", "X"],
    ["X", "X", "X", "", "", "", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "", "", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
],
"pieces": {
    "A": [
        ["X", "X"],
        ["X", "X"]
    ],
    "B": [
        ["X", "X", "", ""],
        ["X", "X", "X", ""],
        ["", "", "X", "X"]
    ],
    "C": [
        ["", "X", ""],
        ["", "X", "X"]
    ]
}

def x_start(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'X':
                print(j)
                return j


def y_start(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] != 'X':
                print(i)
                return i


def x_end(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows-1, -1, -1):
        for j in range(cols):
            if matrix[i][j] != 'X':
                print(j)
                return j


def y_end(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols-1, -1, -1):
        for i in range(rows):
            if matrix[i][j] != 'X':
                print(i)
                return i


def compare_size(matrix1, matrix2, x0, y0):
    length1 = x_end(matrix1) - x0 + 1
    width1 = y_end(matrix1) - y0 + 1
    width2 = len(matrix2)
    length2 = len(matrix2[0])
    print(length1, width1, length2, width2)
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
    x0 = x_start(matrix)
    y0 = y_start(matrix)

    if fits_in(matrix, piece["A"], x0, y0) and compare_size(matrix, piece["A"], x0, y0):
        return "A"
    elif fits_in(matrix, piece["B"], x0, y0) and compare_size(matrix, piece["B"], x0, y0):
        return "B"
    elif fits_in(matrix, piece["C"], x0, y0) and compare_size(matrix, piece["C"], x0, y0):
        return "C"
    else:
        return "None"

algo_reasoning(drawing, pieces)

Why does it return nothing ?