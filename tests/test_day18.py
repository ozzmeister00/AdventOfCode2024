from unittest import TestCase

import solutions.day18


class TestDay18(TestCase):
    def test_part01(self):
        expected = 22
        testData = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''
        solver = solutions.day18.Solver(rawData=testData)

        self.assertEqual(0, solver.SolvePartOne())

    def test_part02(self):
        expected = 0
        testData = ''''''
        solver = solutions.day18.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
