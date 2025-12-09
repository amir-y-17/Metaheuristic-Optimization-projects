from TSP import *
from algorithms.local_search_2opt import local_search_2opt

cities = read_tsp_file()
tsp_instance = TSPInstance(cities)
distance_matrix = tsp_instance.distance_matrix

initial_solution = generate_random_tour(200)
print("Initial distance : ", total_distance(initial_solution, distance_matrix))

print("*" * 50)

optimized_solution = local_search_2opt(initial_solution, distance_matrix)
print("Optimized distance : ", total_distance(optimized_solution, distance_matrix))
