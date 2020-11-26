import unittest
from main import Map


class DFSTest(unittest.TestCase):

    def setUp(self):
        self.map_1 = Map([[0, 1]])
        self.v_1 = [[1, 0]]

        # The second map
        self.map_2 = Map([[1, 0, 1],
                          [0, 0, 1]])
        self.v_2 = [[1, 1, 0],
                    [0, 0, 0]]

        # The third map
        self.map_3 = Map([[1, 0, 1, 1],
                          [1, 0, 1, 1],
                          [0, 0, 0, 1],
                          [1, 0, 1, 0]])
        self.v_3 = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    def tearDown(self):
        self.v_2 = [[1, 1, 0],
                    [0, 0, 0]]
        self.v_3 = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    def test_map(self):
        # Check if the map sizes are calculated correctly
        self.assertEqual(self.map_1.X, 2)
        self.assertEqual(self.map_1.Y, 1)
        self.assertEqual(self.map_2.X, 3)

    def test_validity(self):
        # Check if the cell lies outside the map
        self.assertFalse(self.map_1.is_valid(x=2, y=0, visited=self.v_1))
        self.assertFalse(self.map_2.is_valid(1, 2, self.v_2))

        # Check if the cell has been visited
        self.assertFalse(self.map_1.is_valid(0, 0, self.v_1))
        self.assertFalse(self.map_2.is_valid(0, 0, self.v_2))

        # Check if the cell lies on water
        self.assertFalse(self.map_2.is_valid(1, 1, self.v_2))

        # Check if the cell is a part of an island and has not yet been visited
        self.assertTrue(self.map_1.is_valid(1, 0, self.v_1))
        self.assertTrue(self.map_2.is_valid(2, 1, self.v_2))

    def test_dfs(self):
        # Check if the DFS correctly marks the visited cells
        self.map_2.dfs(2, 0, self.v_2)
        self.assertEqual(self.v_2, [[1, 1, 1],
                                    [0, 0, 1]])
        self.map_3.dfs(3, 0, self.v_3)
        self.assertEqual(self.v_3, [[0, 0, 1, 1],
                                    [0, 0, 1, 1],
                                    [0, 0, 0, 1],
                                    [0, 0, 1, 0]])

    def test_island_count(self):
        self.assertEqual(self.map_1.count_islands(), 1)
        self.assertEqual(self.map_2.count_islands(), 2)
        self.assertEqual(self.map_3.count_islands(), 3)


if __name__ == '__main__':
    unittest.main()
