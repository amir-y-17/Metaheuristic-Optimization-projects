from TSP import *
from algorithms import *


cities = read_tsp_file()
tsp_instance = TSPInstance(cities)
distance_matrix = tsp_instance.distance_matrix

initial_solution = generate_greedy_random_tour(distance_matrix)
print("Initial distance : ", total_distance(initial_solution, distance_matrix))

print("*" * 50)

ls_2_opt_solution = local_search(initial_solution, distance_matrix, operator="2-opt")
print("Local Search 2-opt: ", total_distance(ls_2_opt_solution, distance_matrix))

print("*" * 50)
ls_3_opt_solution = local_search(initial_solution, distance_matrix, operator="3-opt")
print("Local Search 3-opt: ", total_distance(ls_3_opt_solution, distance_matrix))

print("*" * 50)
sa_optimized_solution = SA(
    initial_solution,
    distance_matrix,
    1000,
    0.995,
    1e-3,
    operator="2opt",
)
print(
    "Simulated Annealing 2-opt: ",
    total_distance(sa_optimized_solution, distance_matrix),
)
print("*" * 50)
sa_optimized_solution_3opt = SA(
    initial_solution,
    distance_matrix,
    1000,
    0.995,
    1e-3,
    operator="3opt",
)
print(
    "Simulated Annealing 3-opt: ",
    total_distance(sa_optimized_solution_3opt, distance_matrix),
)
