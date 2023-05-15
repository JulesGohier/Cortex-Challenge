def y_start(matrix, rows, cols):
    """
    Find the starting row index of the '' characters in the matrix
    :param matrix: drawing
    :param rows: numbers of rows in the matrix
    :param cols: numbers of cols in the matrix
    :return: y start
    """
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 'X':
                return j


def x_start(matrix, rows, cols):
    """
    Find the starting column index of the '' characters in the matrix
    :param matrix: drawing
    :param rows: numbers of rows in the matrix
    :param cols: numbers of cols in the matrix
    :return: x start
    """
    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] != 'X':
                return i


def y_end(matrix, rows, cols):
    """
    Find the ending row index of the '' characters in the matrix
    :param matrix: drawing
    :param rows: numbers of rows in the matrix
    :param cols: numbers of cols in the matrix
    :return: y end
    """
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if matrix[i][j] != 'X':
                return j


def x_end(matrix, rows, cols):
    """
    Find the ending column index of the '' characters in the matrix
    :param matrix: drawing
    :param rows: numbers of rows in the matrix
    :param cols: numbers of cols in the matrix
    :return: x end
    """
    for j in range(cols-1, -1, -1):
        for i in range(rows-1, -1, -1):
            if matrix[i][j] != 'X':
                return i


def compare_size(matrix2, length_matrix1, width_matrix1):
    """
    Compare the size of two matrices and return True if they are the same size, False otherwise
    :param matrix2: a piece
    :param length_matrix1: piece length acceptable by the drawing
    :param width_matrix1: piece length acceptable by the drawing
    :return: boolean
    """
    length_matrix2 = len(matrix2)
    width_matrix2 = len(matrix2[0])
    if length_matrix1 == length_matrix2 and width_matrix1 == width_matrix2:
        return True
    else:
        return False


def fits_in(matrix1, matrix2, x0, y0):
    """
    Verify if the piece enter exactly in the drawing
    :param matrix1: drawing
    :param matrix2: piece
    :param x0: locate where the piece inserts in the drawing
    :param y0: locate where the piece inserts in the drawing
    :return: boolean
    """
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    for i in range(rows2):
        for j in range(cols2):
            if matrix1[i + x0][j + y0] == matrix2[i][j]:
                return False
    return True


def algo_reasoning(matrix: list, piece: dict):
    """
    Given a matrix and a dictionary of pieces, determines which piece can fit into the matrix.
    :param matrix: drawing
    :param piece: dict with the pieces
    :return: piece which fits in the drawing
    """
    # Find the starting and ending row and column indices of the '' characters in the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    x0 = x_start(matrix, rows, cols)
    y0 = y_start(matrix, rows, cols)
    length_matrix = x_end(matrix, rows, cols) - x0 + 1  # enlever les variables x0 et y0
    width_matrix = y_end(matrix, rows, cols) - y0 + 1

    # length_piece = len(piece["A"])
    # width_piece = len(piece["A"][0])

    if compare_size(piece["A"], length_matrix, width_matrix):
        if fits_in(matrix, piece["A"], x0, y0):
            return "A"
    if compare_size(piece["B"], length_matrix, width_matrix):
        if fits_in(matrix, piece["B"], x0, y0):
            return "B"
    if compare_size(piece["C"], length_matrix, width_matrix):
        if fits_in(matrix, piece["C"], x0, y0):
            return "C"
    else:
        return "None"
