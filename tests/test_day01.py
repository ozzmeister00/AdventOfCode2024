from unittest import TestCase

import solutions.day01


class TestDay01(TestCase):
    def test_part01(self):
        expected = 11
        testData = '''3   4
4   3
2   5
1   3
3   9
3   3'''
        solver = solutions.day01.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 31
        testData = '''3   4
4   3
2   5
1   3
3   9
3   3'''
        solver = solutions.day01.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
