import random
import matplotlib.pyplot as plt


def total_distance(tour: list, distance_matrix) -> int:
    """Calculate the total distance of the given tour based on the distance matrix."""

    total_dist = 0

    for i in range(len(tour) - 1):
        total_dist += distance_matrix[tour[i]][tour[i + 1]]

    # Return to the starting point
    total_dist += distance_matrix[tour[-1]][tour[0]]

    return total_dist


def generate_random_tour(num_cities: int) -> list:
    """Generate a random tour of the cities."""
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour


def generate_greedy_random_tour(distance_matrix) -> list:
    """Generate a tour using a greedy randomized approach."""

    num_cities = len(distance_matrix)

    # select a random starting city
    start_city = random.randint(0, num_cities - 1)
    tour = [start_city]

    unvisited = set(range(num_cities)) - {start_city}

    while unvisited:
        # 70% chance to choose the nearest neighbor
        if random.random() < 0.7:
            last_city = tour[-1]
            next_city = min(
                unvisited, key=lambda city: distance_matrix[last_city][city]
            )
        else:
            # Randomly select the next city
            next_city = random.choice(list(unvisited))

        tour.append(next_city)
        unvisited.remove(next_city)

    return tour


def nearest_neighbor_tour():
    pass


def plot_tour(points, tour, title="TSP Tour"):
    """
    points: list of [x, y]
    tour: list of city indices in visiting order
    """

    # Extract the ordered points based on the tour
    ordered = [points[i] for i in tour]

    # Separate x and y for plotting
    xs = [p[0] for p in ordered]
    ys = [p[1] for p in ordered]

    plt.figure(figsize=(8, 6))

    # Plot the path
    plt.plot(xs, ys, "-o")

    # Write city numbers next to the points
    for idx, (x, y) in enumerate(ordered):
        plt.text(x, y, str(tour[idx]), fontsize=9)

    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()
