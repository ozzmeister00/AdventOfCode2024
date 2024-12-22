"""
"""
import collections
import functools

import utils.list

import solver.runner
import solver.solver


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        # initialize our mappings
        self.before = collections.defaultdict(list)
        self.after = collections.defaultdict(list)

        self.pageUpdates = []

        super(Solver, self).__init__(5, rawData=rawData)

    def ProcessInput(self) -> None:
        """

        split the input data into two sections, a list of int pairs specifying 
the ordering rule,
         and subsequently the page numbers of each update

        :returns: don't return anything, just stash the data on the class for 
later retrieval
        """
        rules, updates = self.rawData.split('\n\n')

        for rule in rules.splitlines():
            a, b = list(map(int, rule.split('|')))

            # this is a list mapping all the things that A must come BEFORE
            self.before[a].append(b)

            # inversely, this list maps all the things that B must come AFTER
            self.after[b].append(a)

        for update in updates.splitlines():
            self.pageUpdates.append(list(map(int, update.split(','))))

    def sortUpdate(self, update:list[int]) -> list[int]:
        """
        Use a sorting function to determine if the update is in the correct 
order
        """
        def order(a, b):
            if b in self.before[a]:
                return -1
            elif a in self.before[b]:
                return 1
            return 0

        return sorted(update, key=functools.cmp_to_key(order))

    def isUpdateCorrectlyOrdered(self, update: list[int]) -> bool:
        """
        Take the input update and test to see if it's properly sorted based on 
our rules
        :return:
        """
        return update == self.sortUpdate(update)

    def SolvePartOne(self) -> int:
        """

        :return int: the sum of middle page numbers for correctly ordered 
updates
        """
        result = 0

        for update in self.pageUpdates:
            if self.isUpdateCorrectlyOrdered(update):
                result += update[len(update) // 2]

        return result

    def SolvePartTwo(self) -> int:
        """

        :return int: the sum of the middle pages of incorrectly ordered updates 
once they've been correctly ordered
        """
        result = 0

        for update in self.pageUpdates:
            if not self.isUpdateCorrectlyOrdered(update):
                result += self.sortUpdate(update)[len(update) // 2]

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
