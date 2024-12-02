from unittest import TestCase

import solutions.day02


class TestDay02(TestCase):
    def test_validateLine(self):
        testValues = [([7, 6], True), # decreasing by one
                      ([5, 7, 6], False), # not all increasing
                      ([7, 2], False), # decreasing greater than 3
                      ([2, 7], False)] #increasing greater than 3

        for value, expected in testValues:
            self.assertEqual(solutions.day02.Solver.validateLine(value), expected)

    def test_validateLinesSafe(self):
        pass

    def test_part01(self):
        expected = 2
        testData = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
        solver = solutions.day02.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 4
        testData = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
        solver = solutions.day02.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
