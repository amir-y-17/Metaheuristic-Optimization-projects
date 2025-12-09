from TSP import *


def local_search_2opt(initial_tour, distance_matrix):
    """
    Performs local search using the 2-opt algorithm to improve the given tour.
    """

    current = initial_tour
    n = len(initial_tour)

    improved = True
    while improved:
        improved = False

        for i in range(1, n - 2):
            a = current[i - 1]
            b = current[i]

            for k in range(i + 1, n - 1):
                c = current[k]
                d = current[k + 1]

                # Calculate the cost difference if we perform the 2-opt move
                old_cost = distance_matrix[a][b] + distance_matrix[c][d]
                new_cost = distance_matrix[a][c] + distance_matrix[b][d]

                if new_cost < old_cost:
                    current[i : k + 1] = reversed(current[i : k + 1])
                    improved = True
                    break

            if improved:
                break

    return current
