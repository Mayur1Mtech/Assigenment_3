import itertools
import asyncio
import sys

class ShortRoute:
    def __init__(self, cities, dist):
        self.cities = cities
        self.dist = dist
        self.n = len(cities)

        if self.n != len(dist) or any(self.n != len(row) for row in dist):
            raise ValueError("Invalid distance matrix")

        if not all(isinstance(city, str) for city in cities):
            raise ValueError("Invalid city name")

    async def solve(self):
        min_dist = sys.maxsize
        min_path = None

        # Generate all permutations of cities to visit
        for path in itertools.permutations(range(1, self.n)):
            path = (0,) + path + (0,)

            # Compute the total distance of the path
            total_dist = 0
            for i in range(self.n):
                j = i + 1
                total_dist += self.dist[path[i]][path[j]]

            # Update the minimum distance and path if the current path is shorter
            if total_dist < min_dist:
                min_dist = total_dist
                min_path = path

        min_path = [self.cities[i] for i in min_path]
        return min_dist, min_path

async def main():
    cities = []
    dist = []

    try:
        # Get input for number of cities
        n = int(input("Enter number of cities: "))

        # Get input for cities
        print("Enter city names:")
        for i in range(n):
            city = input(f"City {i+1}: ")
            cities.append(city)

        # Get input for distances between cities
        print("Enter distances between cities:")
        for i in range(n):
            row = input(f"Distances from {cities[i]} (separated by spaces): ")
            dist.append(list(map(int, row.split())))

        sr = ShortRoute(cities, dist)
        min_dist, min_path = await sr.solve()
        print("Shortest distance:", min_dist)
        print("Shortest path:", "->".join(min_path))
    except ValueError as e:
        print("Error:", str(e))

if __name__ == "__main__":
    asyncio.run(main())


