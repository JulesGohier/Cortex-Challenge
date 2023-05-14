import networkx as nx


def algo_labyrinth(matrix: list):
    """
    This function allows you to find the exit of the labyrinth (1,2,3 or 4)
    :param matrix: The matrix containing the labyrinth
    :return: The number identifying one of the four possible outputs
    """
    # initialisation of the set of variables
    g = nx.Graph()
    coordinates = []
    row = len(matrix)
    col = len(matrix[0])
    start = (0, 0)
    num_1 = 0
    num_2 = 0
    num_3 = 0
    num_4 = 0
    num_start = 0

    # Adds to a list all the x and y coordinates of all the empty cells and the coordinates of the starting point
    for i in range(row):
        for j in range(col):
            if matrix[i][j] != "X":
                if matrix[i][j] == "D":
                    start = [i, j]
                coordinates.append([i, j])

    # Add all empty cells as points of the graph, x, and y are used for positioning (each point is numbered) and
    # numbering of the four possible outputs.
    for i, (x, y) in enumerate(coordinates):
        if (x, y) == (0, 0):
            num_1 = i
        elif (x, y) == (0, col-1):
            num_2 = i
        elif (x, y) == (row-1, col-1):
            num_3 = i
        elif (x, y) == (row-1, 0):
            num_4 = i
        elif (x, y) == start:
            num_start = i
        g.add_node(i, pos=(x, y))

    # Creation of stops for all points whose empty cells are adjacent
    a = len(coordinates)
    for i in range(a):
        for j in range(i + 1, a):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
                g.add_edge(i, j)

    subgraph = list(nx.connected_components(g))
    # Transformation of each subgraph into a list to find a list containing an output point and the starting point
    for i in subgraph:
        if (num_1 in i) and (num_start in i):
            return 1
        if (num_2 in i) and (num_start in i):
            return 2
        if (num_3 in i) and (num_start in i):
            return 3
        if (num_4 in i) and (num_start in i):
            return 4
