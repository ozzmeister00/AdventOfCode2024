from unittest import TestCase

import solutions.day05

testData = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''


class TestDay05(TestCase):
    def test_isUpdateOrderedCorrectly(self):
        solver = solutions.day05.Solver(rawData=testData)

        self.assertTrue(solver.isUpdateCorrectlyOrdered([75, 47, 61, 53, 29]))
        self.assertFalse(solver.isUpdateCorrectlyOrdered([75, 97, 47, 61, 53]))
        self.assertFalse(solver.isUpdateCorrectlyOrdered([61, 13, 29]))
        self.assertFalse(solver.isUpdateCorrectlyOrdered([97, 13, 75, 29, 47]))

    def test_part01(self):
        expected = 143

        solver = solutions.day05.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartOne())

    def test_part02(self):
        expected = 123
        solver = solutions.day05.Solver(rawData=testData)

        self.assertEqual(expected, solver.SolvePartTwo())

