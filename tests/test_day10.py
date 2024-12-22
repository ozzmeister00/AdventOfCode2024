from unittest import TestCase

import solutions.day10


class TestDay10(TestCase):
    def test_part01(self):
        expected = 36
        testData = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
        solver = solutions.day10.Solver(rawData=testData)

        self.assertEqual(0, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day10.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
