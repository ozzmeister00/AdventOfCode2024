from unittest import TestCase

import solutions.day06

testData = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''


class TestDay06(TestCase):
    def test_part01(self):
        expected = 41
        solver = solutions.day06.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 6
        solver = solutions.day06.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
