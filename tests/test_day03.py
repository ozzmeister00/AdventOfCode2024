from unittest import TestCase

import solutions.day03


class TestDay03(TestCase):
    def test_part01(self):
        expected = 161
        testData = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul mul(11,8)mul(8,5))'''
        solver = solutions.day03.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 48
        testData = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul mul(11,8)undo()?mul(8,5))'''
        solver = solutions.day03.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
