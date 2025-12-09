from TSP import *


def local_search(initial_tour, distance_matrix, operator):
    """
    Perform local search optimization on the given tour using the specified operator.
    """
    operators = {
        "2-opt": apply_2opt,
        "3-opt": apply_3_opt,
    }

    if operator not in operators:
        raise ValueError(f"Unknown operator: {operator}")

    apply_operator = operators[operator]
    current = initial_tour.copy()
    n = len(initial_tour)
    current_distance = total_distance(current, distance_matrix)

    improved = True
    while improved:
        improved = False

        if operator == "2-opt":
            for i in range(1, n - 2):
                a = current[i - 1]
                b = current[i]

                for k in range(i + 1, n - 1):
                    c = current[k]
                    d = current[k + 1]

                    old_cost = distance_matrix[a][b] + distance_matrix[c][d]
                    new_cost = distance_matrix[a][c] + distance_matrix[b][d]

                    if new_cost < old_cost:
                        current[i : k + 1] = reversed(current[i : k + 1])
                        current_distance += new_cost - old_cost
                        improved = True
                        break

                if improved:
                    break

        elif operator == "3-opt":
            # Implementing a simple version of 3-opt local search
            for i in range(1, n - 3):
                for j in range(i + 1, n - 2):
                    for k in range(j + 1, n - 1):

                        new_tour = apply_operator(current, i, j, k, distance_matrix)
                        new_distance = total_distance(new_tour, distance_matrix)

                        if new_distance < current_distance:
                            current = new_tour
                            current_distance = new_distance
                            improved = True
                            break

                    if improved:
                        break
                if improved:
                    break

    return current
