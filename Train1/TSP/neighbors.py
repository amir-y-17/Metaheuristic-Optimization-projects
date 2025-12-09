def apply_2opt(tour: list, i: int, k: int) -> list:
    """
    Apply the 2-opt move to the given tour by reversing the segment between indices i and k.
    """
    new_tour = tour[:i] + tour[i : k + 1][::-1] + tour[k + 1 :]
    return new_tour
