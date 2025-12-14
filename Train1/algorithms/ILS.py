import random
from TSP import *
from algorithms.local_search import local_search


def ILS(
    initial_tour,
    distance_matrix,
    max_iterations=100,
    perturbation_strength=2,
    operator="2-opt",
):
    """
    Perform Iterated Local Search (ILS) on the given initial tour.
    """

    current_local_optimum = initial_tour.copy()
    current_distance = total_distance(current_local_optimum, distance_matrix)

    best_tour = current_local_optimum
    best_tour_distance = current_distance

    for _ in range(max_iterations):

        # Perturbation: randomly swap 'perturbation_strength' pairs of cities
        perturbed_tour = current_local_optimum.copy()
        n = len(perturbed_tour)

        for _ in range(perturbation_strength):
            i, j = random.sample(range(1, n), 2)  # Avoid swapping the starting city
            perturbed_tour[i], perturbed_tour[j] = (
                perturbed_tour[j],
                perturbed_tour[i],
            )

        # Local Search on the perturbed tour
        new_local_optimum = local_search(
            perturbed_tour, distance_matrix, operator=operator
        )
        new_distance = total_distance(new_local_optimum, distance_matrix)

        # Acceptance Criterion
        if new_distance < current_distance:
            current_local_optimum = new_local_optimum
            current_distance = new_distance

            # Update best tour found
            if new_distance < best_tour_distance:
                best_tour = new_local_optimum
                best_tour_distance = new_distance

    return best_tour
