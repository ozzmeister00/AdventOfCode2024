"""
"""
import collections
import itertools
from typing import Iterable

import solver.runner
import solver.solver

import utils.math


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        self.equations = []

        super(Solver, self).__init__(7, rawData=rawData)

    def ProcessInput(self) :
        """
        :returns:
        """
        for line in self.rawData.splitlines():
            answer, equation = line.split(': ')
            operands = list(map(int, equation.split(' ')))
            self.equations.append([int(answer)] + operands)

    def sumValidEquations(self, operations: Iterable) -> int:
        """
        Using the list of input operations, determine the sum of valid equations

        :param operations: list of math functions
        :return: the usm of valid equations
        """
        result = 0

        # cache off operation combinations once they've been generated
        operationCombinations = collections.defaultdict(list)

        # this is apparently legal!
        for answer, *operands in self.equations:
            numOperations = len(operands) - 1
            if numOperations not in operationCombinations:
                operationCombinations[numOperations] = list(itertools.product(operations, repeat=numOperations))

            isValid = False
            combinationIndex = 0
            while not isValid and combinationIndex < len(operationCombinations[numOperations]):
                operandIndex = 0
                value = operands[operandIndex]
                for nextValue in operands[1:]:
                    value = operationCombinations[numOperations][combinationIndex][operandIndex](value, nextValue)
                    operandIndex += 1

                isValid = value == answer

                combinationIndex += 1

            if isValid:
                result += answer

        return result

    def SolvePartOne(self) -> int:
        """

        :return int: the sum of test values from just equation that are solvably
 true
        """
        operations = [utils.math.add, utils.math.mul]

        return self.sumValidEquations(operations)

    def SolvePartTwo(self) -> int:
        """

        :return int: the result
        """
        operations = [utils.math.add, utils.math.mul, concat]

        return self.sumValidEquations(operations)


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
