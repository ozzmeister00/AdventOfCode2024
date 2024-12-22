from unittest import TestCase

import solutions.day16


class TestDay16(TestCase):
    def test_part01(self):
        expected = 7036
        testData = '''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''
        solver = solutions.day16.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day16.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
