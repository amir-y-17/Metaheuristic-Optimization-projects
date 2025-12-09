import math
import random
from TSP import *


def SA_2opt(initial_tour, distance_matrix, initial_temp, cooling_rate, stopping_temp):

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
            i, k = random.sample(range(n), 2)
            new_tour = apply_2opt(current, min(i, k), max(i, k))
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
