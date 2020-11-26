import sys
import os

class Map:

    def __init__(self, g, path=None):
        self.graph = g if path is None else self.load_graph(path)
        self.X = len(self.graph[0])
        self.Y = len(self.graph)

    def load_graph(self, path):
        with open(path) as txt:
            return [[int(x) for x in line if x != '\n'] for line in txt]

    def is_valid(self, x, y, visited):
        return (0 <= x < self.X and
                0 <= y < self.Y and
                not visited[y][x] and self.graph[y][x])

    def dfs(self, x, y, visited):
        # Neighbouring cell coords
        rows = [-1, -1, -1,  0, 0,  1, 1, 1]
        cols = [-1,  0,  1, -1, 1, -1, 0, 1]

        # Mark the cell as visited
        visited[y][x] = 1

        # Recur for all neighbouring cells
        for i in range(8):
            if self.is_valid(x + cols[i], y + rows[i], visited):
                self.dfs(x + cols[i], y + rows[i], visited)

    def count_islands(self):
        # All cells are unvisited at the start
        visited = [[0 for x in range(self.X)]for y in range(self.Y)]

        # Go through all the cells in the map
        count = 0
        for y in range(self.Y):
            for x in range(self.X):
                if visited[y][x] == 0 and self.graph[y][x] == 1:
                    # New island found
                    self.dfs(x, y, visited)
                    count += 1
        return count


if __name__ == '__main__':
    if os.path.exists(sys.argv[1]):
        m = Map(g=None, path=sys.argv[1])
        print(m.count_islands())
    else:
        print(f"The file '{sys.argv[1]}' doesn't exist", file=sys.stderr)

