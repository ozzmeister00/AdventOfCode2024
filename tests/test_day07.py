
from unittest import TestCase

import solutions.day07


TEST_DATA = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''


class TestDay07(TestCase):
    def test_part01(self):
        expected = 3749
        solver = solutions.day07.Solver(rawData=TEST_DATA)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 11387
        solver = solutions.day07.Solver(rawData=TEST_DATA)

        self.assertEqual(expected, solver.SolvePartTwo())
