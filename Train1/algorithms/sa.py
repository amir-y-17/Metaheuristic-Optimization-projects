import math
import random
from TSP import *


def SA(
    initial_tour,
    distance_matrix,
    initial_temp,
    cooling_rate,
    stopping_temp,
    operator,
):
    """
    Performs Simulated Annealing to optimize the given tour using the specified neighborhood operator.
    """

    # -------- Define neighborhood operators --------
    operators = {"2opt": apply_2opt, "3opt": apply_3_opt}
    apply_operator = operators[operator]

    current = initial_tour.copy()
    best = initial_tour.copy()

    current_distance = total_distance(current, distance_matrix)
    best_distance = current_distance

    n = len(current)
    T = initial_temp
    T_min = stopping_temp

    no_improvement = 0
    L = n * 5  # Number of iterations at each temperature

    while T > T_min and no_improvement < 20:

        improved = False

        for _ in range(L):
            if operator == "2opt":
                i, k = random.sample(range(n), 2)
                new_tour = apply_operator(current, min(i, k), max(i, k))

            elif operator == "3opt":
                i, j, k = sorted(random.sample(range(n), 3))
                new_tour = apply_operator(current, i, j, k, distance_matrix)

            new_distance = total_distance(new_tour, distance_matrix)
            delta = new_distance - current_distance

            if delta <= 0:
                current = new_tour
                current_distance = new_distance
                improved = True

                if new_distance < best_distance:
                    best = new_tour
                    best_distance = new_distance

            else:
                P = math.exp(-delta / T)
                if random.random() < P:
                    current = new_tour
                    current_distance = new_distance

        T *= cooling_rate

        if improved:
            no_improvement = 0
        else:
            no_improvement += 1

    return best
