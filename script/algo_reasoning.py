def extract_shape(matrix: list):
    """
    A function that extracts the shape of the piece in the matrix that contains the missing piece
    :param matrix: The matrix containing the missing part
    :return: Returns the shape matrix of the missing piece
    """
    shape_matrix = []
    min_column = len(matrix[0]) - 1
    max_column = 0

    for row in matrix:
        shape_row = []
        for column_number, element_row in enumerate(row):
            if element_row == '':
                shape_row.append("X")
                min_column = min(min_column, column_number)
                max_column = max(max_column, column_number)
            else:
                shape_row.append('')
        if any(shape_row):
            shape_matrix.append(shape_row)

    matrix_part = []
    for row in shape_matrix:
        matrix_part.append(row[min_column:max_column + 1])

    return matrix_part


def compare_matrices(matrix1: list, matrix2: list):
    """
    This function allows to compare two matrices to know if they are identical
    :param matrix1: Matrix to check
    :param matrix2: Matrix to check
    :return: Returns true if identical is not false
    """
    if len(matrix1) != len(matrix2):
        return False

    for row_matrix1, row_matrix2 in zip(matrix1, matrix2):
        if len(row_matrix1) != len(row_matrix2):
            return False
        for element_matrix1, element_matrix2 in zip(row_matrix1, row_matrix2):
            if element_matrix1 != element_matrix2:
                return False

    return True


def algo_reasoning(matrix: list, part: dict):
    """
    This function combines the two previous functions and returns the key to the missing piece of the puzzle.
    :param matrix: Matrix that contains the missing part
    :param part: Dictionary of puzzle pieces. The pattern: the key is a letter and the value is the matrix of the piece
    :return: Returns the letter associated with the correct part
    """
    if compare_matrices(extract_shape(matrix), part["A"]):
        return"A"
    elif compare_matrices(extract_shape(matrix), part["B"]):
        return "B"
    elif compare_matrices(extract_shape(matrix), part["C"]):
        return "C"
