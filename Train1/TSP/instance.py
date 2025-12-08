import math


def build_distance_matrix(coords):
    """
    Compute the distance matrix for a list of coordinates.
    """
    n = len(coords)
    distances = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            dx = coords[i][0] - coords[j][0]
            dy = coords[i][1] - coords[j][1]
            dist = round(math.sqrt(dx**2 + dy**2))
            distances[i][j] = dist
            distances[j][i] = dist

    return distances


class TSPInstance:
    """
    Class representing a TSP instance with coordinates and distance matrix.
    """

    def __init__(self, coords):
        self.coords = coords
        self.distance_matrix = build_distance_matrix(coords)
