from unittest import TestCase

import solutions.day17


class TestDay17(TestCase):
    def test_part01(self):
        expected = [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]
        testData = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''
        solver = solutions.day17.Solver(rawData=testData)

        self.assertEqual(0, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day17.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
