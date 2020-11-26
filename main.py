class Map:

    def __init__(self, g):
        self.X = len(g[0])
        self.Y = len(g)
        self.graph = g

    def is_valid(self, x, y, visited):
        pass

    def dfs(self):
        pass

    def count_islands(self):
        pass


if __name__ == '__main__':
    graph = [[]]

    m = Map(graph)
    print(m.count_islands())

