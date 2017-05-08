#!/usr/bin/env python3

import unittest
import ch


class ChTest(unittest.TestCase):

    def setUp(self):
        self.points = [[0, 7], [2, 5], [4, 4], [3, 9], [6, 8], [9, 6], [6, 4],
                       [7, 2], [9, 1]]

    def test_insert(self):
        points = []
        ch.insert(points, [9, 0])
        ch.insert(points, [1, 9])
        ch.insert(points, [5, 4])
        ch.insert(points, [2, 4])

        self.assertEqual(points, [[1, 9], [2, 4], [5, 4], [9, 0]])

    def test_lower_y(self):
        self.assertEqual(8, ch.lower_y(self.points))

    def test_higher_y(self):
        self.assertEqual(3, ch.higher_y(self.points))

    def test_f(self):
        self.assertEqual(10, ch.f([3, 2], [8, 7], 11))
        self.assertEqual(4, ch.f([0, 8], [6, 0], 3))

    def test_above(self):
        self.assertEqual(True, ch.above([3, 2], [8, 7], [11, 11]))
        self.assertEqual(True, ch.above([3, 2], [8, 7], [3, 5]))
        self.assertEqual(True, ch.above([0, 8], [6, 0], [3, 5]))

    def test_below(self):
        self.assertEqual(True, ch.below([3, 2], [8, 7], [10, 6]))
        self.assertEqual(True, ch.below([3, 2], [8, 7], [3, -4]))
        self.assertEqual(True, ch.below([0, 8], [6, 0], [3, 3]))

    def test_prev(self):
        p1 = [[4, 4], [2, 5], [0, 7], [3, 9], [6, 8]]
        self.assertEqual(0, ch.prev(p1, 1))
        self.assertEqual(4, ch.prev(p1, 0))

    def test_next(self):
        p1 = [[4, 4], [2, 5], [0, 7], [3, 9], [6, 8]]
        self.assertEqual(1, ch.next(p1, 0))
        self.assertEqual(0, ch.next(p1, 4))

    def test_points_to_connect_upper_inner_move(self):
        p1 = [[4, 4], [2, 5], [0, 7], [3, 9], [6, 8]]
        p2 = [[9, 1], [7, 2], [6, 4], [9, 6]]
        self.assertEqual((4, 3), ch.points_to_connect_upper(p1, p2))

    def test_points_to_connect_lower_inner_move(self):
        p1 = [[4, 4], [2, 5], [0, 7], [3, 9], [6, 8]]
        p2 = [[9, 1], [7, 2], [6, 4], [9, 6]]
        self.assertEqual((1, 1), ch.points_to_connect_lower(p1, p2))

    def test_points_to_connect_lower_outer_move(self):
        p1 = [[5, 5], [3, 7], [4, 8]]
        p2 = [[6, 2], [7, 9]]
        self.assertEqual((1, 0), ch.points_to_connect_lower(p1, p2))

    def test_combine(self):
        p1 = [[4, 4], [2, 5], [0, 7], [3, 9], [6, 8]]
        p2 = [[9, 1], [7, 2], [6, 4], [9, 6]]
        h = [[2, 5], [0, 7], [3, 9], [6, 8], [9, 6], [9, 1], [7, 2]]
        self.assertEqual(h, ch.combine(p1, p2))

    def test_combine_two_points_same_x(self):
        p1 = [[2, 2]]
        p2 = [[2, 4]]
        self.assertEqual([[2, 2], [2, 4]], ch.combine(p1, p2))

    def test_convex_hull(self):
        points = [[2, 2], [2, 4]]
        self.assertEqual([[2, 2], [2, 4]], ch.convex_hull(points))

    def test_convex_hull_1(self):
        points = [[1, 1], [2, 5], [3, 3], [5, 3], [3, 2], [2, 2]]
        self.assertEqual([[1, 1], [2, 5], [5, 3], [3, 2]],
                         ch.convex_hull(points))

    def test_convex_hull_two_squares(self):
        points = [[4, 6], [6, 6], [4, 8], [6, 8],
                  [3, 4], [1, 4], [1, 1], [3, 1]]
        hull = [[3, 1], [1, 1], [1, 4], [4, 8], [6, 8], [6, 6]]
        self.assertEqual(hull, ch.convex_hull(points))

if __name__ == '__main__':
    unittest.main()
