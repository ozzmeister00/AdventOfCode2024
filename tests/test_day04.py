from unittest import TestCase

import solutions.day04


class TestDay04(TestCase):
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

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day04.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
