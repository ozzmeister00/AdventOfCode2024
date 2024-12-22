from unittest import TestCase

import solutions.day19


class TestDay19(TestCase):
    def test_part01(self):
        expected = 6
        testData = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''
        solver = solutions.day19.Solver(rawData=testData)

        self.assertEqual(0, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day19.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
