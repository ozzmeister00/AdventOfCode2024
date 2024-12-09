from unittest import TestCase

import solutions.day01


class TestDay01(TestCase):
    def test_part01(self):
        expected = 0
        testData = ''''''
        solver = solutions.day01.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day01.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
