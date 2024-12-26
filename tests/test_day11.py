from unittest import TestCase

import solutions.day11


class TestDay11(TestCase):
    def test_part01(self):
        expected = 55312
        testData = '''125 17'''
        solver = solutions.day11.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())
