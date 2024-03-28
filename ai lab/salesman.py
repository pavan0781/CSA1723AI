#9 Travelling Salesman Problem

import itertools

def distance(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])

def total_distance(path, cities):
    total = 0
    for i in range(len(path) - 1):
        total += distance(cities[path[i]], cities[path[i + 1]])
    total += distance(cities[path[-1]], cities[path[0]])  # Return to starting city
    return total

def brute_force_tsp(cities):
    num_cities = len(cities)
    min_distance = float('inf')
    best_path = []

    for path in itertools.permutations(range(num_cities)):
        d = total_distance(path, cities)
        if d < min_distance:
            min_distance = d
            best_path = path

    return best_path, min_distance

# Get user input for cities
num_of_cities = int(input("Enter the number of cities: "))
cities = []
for i in range(num_of_cities):
    x, y = map(int, input(f"Enter coordinates for city {i+1} (x y): ").split())
    cities.append((x, y))

best_path, min_distance = brute_force_tsp(cities)
print("Best Path:", best_path)
print("Min Distance:", min_distance)
