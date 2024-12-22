from unittest import TestCase

import solutions.day21


class TestDay01(TestCase):
    def test_part01(self):
        expected = 126384
        testData = '''029A
980A
179A
456A
379A'''
        solver = solutions.day21.Solver(rawData=testData)

        self.assertEqual(0, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day21.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
