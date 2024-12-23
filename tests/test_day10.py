from unittest import TestCase

import solutions.day10


class TestDay10(TestCase):
    def test_part01(self):
        simpleTest = '''...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
'''
        simpleExpected = 2

        solver = solutions.day10.Solver(rawData=simpleTest)
        self.assertEqual(simpleExpected, solver.SolvePartOne())

        testTwo = '''..90..9
...1.98
...2..7
6543456
765.987
876....
987....'''
        resultTwo = 4

        solver = solutions.day10.Solver(rawData=testTwo)
        self.assertEqual(resultTwo, solver.SolvePartOne())

        expected = 36
        testData = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
        solver = solutions.day10.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 81
        testData = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
        solver = solutions.day10.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())
