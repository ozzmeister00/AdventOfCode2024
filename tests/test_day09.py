from unittest import TestCase

import solutions.day09


class TestDay09(TestCase):
    def test_part01(self):
        expected = 1928
        testData = '''2333133121414131402'''
        solver = solutions.day09.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 2858
        testData = '''2333133121414131402'''
        solver = solutions.day09.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
