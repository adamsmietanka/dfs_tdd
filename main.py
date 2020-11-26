class Map:

    def __init__(self, x, y, g):
        self.X = x
        self.Y = y
        self.graph = graph

    def is_valid(self):
        pass

    def dfs(self):
        pass

    def count_islands(self):
        pass


if __name__ == '__main__':
    graph = [[]]

    x = len(graph)
    y = len(graph[0])
    m = Map(x, y, graph)
    print(m.count_islands())

