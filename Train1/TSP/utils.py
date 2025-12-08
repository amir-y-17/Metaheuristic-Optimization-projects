def total_distance(tour: list, distance_matrix) -> int:
    """Calculate the total distance of the given tour based on the distance matrix."""

    total_dist = 0

    for i in range(len(tour) - 1):
        total_dist += distance_matrix[tour[i]][tour[i + 1]]

    # Return to the starting point
    total_dist += distance_matrix[tour[-1]][tour[0]]

    return total_dist


def generate_random_tour():
    pass


def nearest_neighbor_tour():
    pass


def plot_tour():
    pass
