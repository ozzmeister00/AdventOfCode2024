from unittest import TestCase

import solutions.day14


class TestDay14(TestCase):
    def test_part01(self):
        expected = 12
        testData = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
        solver = solutions.day14.Solver(rawData=testData, width=11, height=7)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        self.skipTest("not ready")
        expected = 0
        testData = ''''''
        solver = solutions.day14.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
