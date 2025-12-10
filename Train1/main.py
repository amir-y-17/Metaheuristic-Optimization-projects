from TSP import *
from algorithms import *


def run_local_search_2opt(tsp_instance, distance_matrix, initial_solution):
    print(f"Initial distance: {total_distance(initial_solution, distance_matrix)}")
    print("**" * 50)
    print("\nRunning Local Search 2-opt...")
    sol = local_search(initial_solution, distance_matrix, operator="2-opt")
    print("Distance:", total_distance(sol, distance_matrix))
    plot_tour(
        tsp_instance.coords,
        sol,
        title=f"Local Search 2-opt Distance: {total_distance(sol, distance_matrix)}",
    )


def run_local_search_3opt(tsp_instance, distance_matrix, initial_solution):
    print(f"Initial distance: {total_distance(initial_solution, distance_matrix)}")
    print("**" * 50)
    print("\nRunning Local Search 3-opt...")
    sol = local_search(initial_solution, distance_matrix, operator="3-opt")
    print("Distance:", total_distance(sol, distance_matrix))
    plot_tour(
        tsp_instance.coords,
        sol,
        title=f"Local Search 3-opt Distance: {total_distance(sol, distance_matrix)}",
    )


def run_sa_2opt(tsp_instance, distance_matrix, initial_solution):
    print(f"Initial distance: {total_distance(initial_solution, distance_matrix)}")
    print("**" * 50)
    print("\nRunning Simulated Annealing 2-opt...")
    sol = SA(initial_solution, distance_matrix, 1000, 0.995, 1e-3, operator="2opt")
    print("Distance:", total_distance(sol, distance_matrix))
    plot_tour(
        tsp_instance.coords,
        sol,
        title=f"SA 2-opt Distance: {total_distance(sol, distance_matrix)}",
    )


def run_sa_3opt(tsp_instance, distance_matrix, initial_solution):
    print(f"Initial distance: {total_distance(initial_solution, distance_matrix)}")
    print("**" * 50)
    print("\nRunning Simulated Annealing 3-opt...")
    sol = SA(initial_solution, distance_matrix, 1000, 0.995, 1e-3, operator="3opt")
    print("Distance:", total_distance(sol, distance_matrix))
    plot_tour(
        tsp_instance.coords,
        sol,
        title=f"SA 3-opt Distance: {total_distance(sol, distance_matrix)}",
    )


def main_menu():
    cities = read_tsp_file()
    tsp_instance = TSPInstance(cities)
    distance_matrix = tsp_instance.distance_matrix

    initial_solution = generate_greedy_random_tour(distance_matrix)
    print("Initial distance:", total_distance(initial_solution, distance_matrix))

    while True:
        print("\n" + "=" * 50)
        print(" TSP Algorithm Menu ")
        print("=" * 50)
        print("1. Local Search (2-opt)")
        print("2. Local Search (3-opt)")
        print("3. Simulated Annealing (2-opt)")
        print("4. Simulated Annealing (3-opt)")
        print("0. Exit")
        print("=" * 50)

        choice = input("Choose an option: ").strip()
        print("=" * 50)

        if choice == "1":
            run_local_search_2opt(tsp_instance, distance_matrix, initial_solution)

        elif choice == "2":
            run_local_search_3opt(tsp_instance, distance_matrix, initial_solution)

        elif choice == "3":
            run_sa_2opt(tsp_instance, distance_matrix, initial_solution)

        elif choice == "4":
            run_sa_3opt(tsp_instance, distance_matrix, initial_solution)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main_menu()
