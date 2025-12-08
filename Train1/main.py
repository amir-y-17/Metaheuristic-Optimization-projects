from TSP import *
import numpy as np

cities = read_tsp_file()
tsp_instance = TSPInstance(cities)
distance_matrix = tsp_instance.distance_matrix

print("Generating greedy randomized tour...")
tour = generate_greedy_random_tour(distance_matrix)

print("Tour:", tour)
print("Total distance:", total_distance(tour, distance_matrix))
