from TSP import *
from algorithms import *


cities = read_tsp_file()
tsp_instance = TSPInstance(cities)
distance_matrix = tsp_instance.distance_matrix

initial_solution = generate_random_tour(200)
print("Initial distance : ", total_distance(initial_solution, distance_matrix))

print("*" * 50)

optimized_solution = local_search_2opt(initial_solution, distance_matrix)
print("Local Search 2-opt: ", total_distance(optimized_solution, distance_matrix))

print("*" * 50)
sa_optimized_solution = SA_2opt(
    initial_solution,
    distance_matrix,
    1000,
    0.995,
    1e-3,
)
print(
    "Simulated Annealing 2-opt: ",
    total_distance(sa_optimized_solution, distance_matrix),
)
