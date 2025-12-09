def apply_2opt(tour, i, k):
    """
    returns a new tour with segment i..k reversed.
    """
    new_tour = tour.copy()
    # Reverse in-place for better performance
    while i < k:
        new_tour[i], new_tour[k] = new_tour[k], new_tour[i]
        i += 1
        k -= 1
    return new_tour


def apply_3_opt(tour, i, j, k, distance_matrix):
    """
    Performs a 3-opt move on the given tour between indices i, j, and k.
    Considers all 7 possible reconnections and returns the best improved tour.
    """

    n = len(tour)

    # Extract segments
    A = tour[0:i]
    B = tour[i:j]
    C = tour[j:k]
    D = tour[k:n]

    # Precompute old edges for delta calculation
    old = (
        distance_matrix[tour[i - 1]][tour[i]]
        + distance_matrix[tour[j - 1]][tour[j]]
        + distance_matrix[tour[k - 1]][tour[k]]
    )

    # Generate all 7 possible reconnects
    candidates = []

    # 1) A + reverse(B) + C + D
    candidates.append(A + B[::-1] + C + D)

    # 2) A + B + reverse(C) + D
    candidates.append(A + B + C[::-1] + D)

    # 3) A + reverse(B) + reverse(C) + D
    candidates.append(A + B[::-1] + C[::-1] + D)

    # 4) A + C + B + D
    candidates.append(A + C + B + D)

    # 5) A + C[::-1] + B + D
    candidates.append(A + C[::-1] + B + D)

    # 6) A + C + B[::-1] + D
    candidates.append(A + C + B[::-1] + D)

    # 7) A + C[::-1] + B[::-1] + D
    candidates.append(A + C[::-1] + B[::-1] + D)

    best_tour = tour
    best_delta = 0  # Only accept if improved (Δ < 0)

    for new_tour in candidates:
        # Compute new edges (only the 3 new connecting edges)
        new = (
            distance_matrix[new_tour[i - 1]][new_tour[i]]
            + distance_matrix[new_tour[j - 1]][new_tour[j]]
            + distance_matrix[new_tour[k - 1]][new_tour[k]]
        )

        delta = new - old

        if delta < best_delta:
            best_delta = delta
            best_tour = new_tour

    return best_tour
