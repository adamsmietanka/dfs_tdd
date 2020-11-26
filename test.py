import unittest
from main import Map


class DFSTest(unittest.TestCase):

    def setUp(self):
        m = [[1, 0, 1],
             [0, 0, 1]]
        self.map_1 = Map([[0, 1]])
        self.map_2 = Map(m)
        self.visited_1 = [[1, 0]]
        self.visited_2 = [[1, 1, 0],
                          [0, 0, 0]]

    def test_map(self):
        # Check if the map sizes are calculated correctly
        self.assertEqual(self.map_1.X, 2)
        self.assertEqual(self.map_1.Y, 1)
        self.assertEqual(self.map_2.X, 3)

    def test_validity(self):
        # Check if the point lies on the map
        self.assertTrue(self.map_1.is_valid(x=1, y=0, visited=self.visited_1))
        self.assertFalse(self.map_1.is_valid(2, 0, self.visited_1))
        self.assertTrue(self.map_2.is_valid(1, 1, self.visited_2))
        self.assertFalse(self.map_2.is_valid(1, 2, self.visited_2))

        # Check if the point has been visited
        self.assertFalse(self.map_2.is_valid(1, 0, self.visited_2))
        self.assertFalse(self.map_2.is_valid(0, 0, self.visited_2))

        # Check if the point is an island
        self.assertTrue(self.map_1.is_valid(1, 0, self.visited_1))


if __name__ == '__main__':
    unittest.main()
