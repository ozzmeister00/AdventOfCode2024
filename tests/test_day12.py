from unittest import TestCase

import solutions.day12
import utils.math

TEST_DATA = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

class TestDay12(TestCase):
    def test_part01(self):
        expected = 1930
        solver = solutions.day12.Solver(rawData=TEST_DATA)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_findNumSides(self):
        solver = solutions.day12.Solver(rawData='A')
        expected = 4
        result = solver.getNumSidesOfRegion([utils.math.Int2(0, 0)])
        self.assertEqual(expected, result)

        solver = solutions.day12.Solver(rawData='AA')
        expected = 4
        twoPoints = solver.getNumSidesOfRegion([utils.math.Int2(0, 0), utils.math.Int2(1, 0)])
        self.assertEqual(expected, twoPoints)

        solver = solutions.day12.Solver(rawData='AB\nAA')
        expected = 6
        lShaped = solver.getNumSidesOfRegion([utils.math.Int2(0,0), utils.math.Int2(0, 1), utils.math.Int2(1, 1)])
        self.assertEqual(expected, lShaped)

        solver = solutions.day12.Solver(rawData='AB\nAA')
        expected = 6
        lShaped = solver.getNumSidesOfRegion([utils.math.Int2(0,0), utils.math.Int2(0, 1), utils.math.Int2(1, 1)])
        self.assertEqual(expected, lShaped)

    def test_part02_simple(self):
        testData = '''AAAA
BBCD
BBCC
EEEC'''
        expected = 80
        solver = solutions.day12.Solver(rawData=testData)
        self.assertEqual(expected, solver.SolvePartTwo())        


    def test_part02_medium(self):
        testData = '''EEEEE
EXXXX
EEEEE
EXXXX
EEEEE'''
        expected = 236
        solver = solutions.day12.Solver(rawData=testData)
        result = solver.SolvePartTwo()
        self.assertEqual(expected, result)

    def test_doubleSidedRegions(self):
        testData = '''AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''
        expected = 368
        solver = solutions.day12.Solver(rawData=testData)
        result = solver.SolvePartTwo()
        self.assertEqual(expected, result)

    def test_part02_large(self):
        expected = 1206
        solver = solutions.day12.Solver(rawData=TEST_DATA)
        result = solver.SolvePartTwo()
        self.assertEqual(expected, result)


# expected number of sides

# R = 10
# I = 4
# C = 22
# F = 12
# V = 10
# J = 12
# C = 4
# E = 8
# I = 16
# M = 6
# S = 6


'''
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''