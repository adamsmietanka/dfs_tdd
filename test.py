import unittest
from main import Map


class DFSTest(unittest.TestCase):

    def test_map(self):
        g = [[1, 0]]
        m = Map(g)
        self.assertEqual(m.X, 2)
        self.assertEqual(m.Y, 1)


if __name__ == '__main__':
    unittest.main()
