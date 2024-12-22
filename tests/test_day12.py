from unittest import TestCase

import solutions.day12


class TestDay12(TestCase):
    def test_part01(self):
        expected = 1930
        testData = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
        solver = solutions.day12.Solver(rawData=testData)

        self.assertEqual(0, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day12.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
