class Map:

    def __init__(self, g):
        self.X = len(g[0])
        self.Y = len(g)
        self.graph = g

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
        pass


if __name__ == '__main__':
    graph = [[]]

    m = Map(graph)
    print(m.count_islands())

