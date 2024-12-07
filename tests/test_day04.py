from unittest import TestCase

import utils.math

import solutions.day04


class TestDay04(TestCase):
    def test_findXMasInDirection(self):
        testData = 'XMAS\nSMAX\n**A*\n***S\nSAMX'

        solver = solutions.day04.Solver(rawData=testData)

        self.assertEqual(False, solver.findXMasInDirection(utils.math.Int2(0, 0), utils.math.Grid2D.North))
        self.assertEqual(True, solver.findXMasInDirection(utils.math.Int2(0, 0), utils.math.Grid2D.East))
        self.assertEqual(True, solver.findXMasInDirection(utils.math.Int2(0, 0), utils.math.Grid2D.NorthEast))
        self.assertEqual(False, solver.findXMasInDirection(utils.math.Int2(3, 1), utils.math.Grid2D.West))
        self.assertEqual(True, solver.findXMasInDirection(utils.math.Int2(3, 4), utils.math.Grid2D.West))

    def test_findXmases(self):
        testData = 'XMAS\nSMAX\n**A*\n***S\nSAMX'
        solver = solutions.day04.Solver(rawData=testData)

        expected = 2
        self.assertEqual(expected, solver.findXMas(utils.math.Int2(0, 0)))

        expected = 0
        self.assertEqual(expected, solver.findXMas(utils.math.Int2(3, 1)))

        expected = 1
        self.assertEqual(expected, solver.findXMas(utils.math.Int2(3, 4)))

    def test_part01(self):
        expected = 18
        testData = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
        solver = solutions.day04.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_isCoordMAS(self):
        masX = '''S.M\n.A.\nS.M'''
        notMasX = '''A.M\n.A.\nS.M'''

        validSolver = solutions.day04.Solver(rawData=masX)
        invalidSolver = solutions.day04.Solver(rawData=notMasX)

        self.assertEqual(True, validSolver.isCoordMAS(utils.math.Int2(1,1)))
        self.assertEqual(False, invalidSolver.isCoordMAS(utils.math.Int2(1, 1)))

    def test_part02(self):
        expected = 9
        testData = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
        solver = solutions.day04.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
