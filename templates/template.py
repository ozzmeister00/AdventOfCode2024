"""
"""

import solver.runner
import solver.solver


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__("$DAY", rawData=rawData)

    def ProcessInput(self):
        """
        :returns:
        """
        processed = None
        return processed

    def SolvePartOne(self) -> int:
        """

        :return int: the result
        """
        result = 0

        return result

    def SolvePartTwo(self) -> int:
        """

        :return int: the result
        """
        result = 0

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
