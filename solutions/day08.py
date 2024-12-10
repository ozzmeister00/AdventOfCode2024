"""
"""
import collections
import itertools

import solver.runner
import solver.solver

import utils.math

EMPTY = '.'

class Antenna(object):
    def __init__(self, frequency: str, position: utils.math.Int2):
        self.frequency = frequency
        self.position = position

    def __str__(self) -> str:
        return self.frequency


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        self.nodeGrid = utils.math.Grid2D(0, data='')
        self.nodeMap = collections.defaultdict(list)
        self.antiNodeGrid = utils.math.Grid2D(0, data='')
        self.antiNodes = []

        super(Solver, self).__init__(8, rawData=rawData)

    def ProcessInput(self):
        """
        Process the input map into a grid of nodes
        as well as initializing a separate grid for mapping the antinodes
        """
        width = len(self.rawData.splitlines()[0])
        self.nodeGrid = utils.math.Grid2D(width, data=self.rawData.replace('\n', ''))

        # build a map of all the antennae
        for coord, value in self.nodeGrid.enumerateCoords():
            if value != EMPTY:
                self.nodeMap[value].append(Antenna(value, coord))

        # initialize a separate grid for visualizing the antinodes
        self.antiNodeGrid = utils.math.Grid2D(width, [0] * len(self.nodeGrid))

    def SolvePartOne(self) -> int:
        """
        :return int: the total number of unique antinode locations *on* the map
        """
        # build a list of combinations of nodes of the same frequency
        nodeCombinations = []
        for frequency in self.nodeMap:
            if len(self.nodeMap[frequency]) > 1:
                nodeCombinations += list(itertools.combinations(self.nodeMap[frequency], 2))

        for a, b in nodeCombinations:
            # get the directions from A to B and B to A and add that vector to the respective node to get its antinode
            aToB = b.position - a.position
            bToA = a.position - b.position

            antinodeA = a.position + bToA
            antinodeB = b.position + aToB

            if self.nodeGrid.coordsInBounds(antinodeA):
                self.antiNodes.append(antinodeA)

            if self.nodeGrid.coordsInBounds(antinodeB):
                self.antiNodes.append(antinodeB)

        return len(set(self.antiNodes))

    def SolvePartTwo(self) -> int:
        """

        :return int: the number of unique antinodes, when accounting for resonance
        """
        # build a list of combinations of nodes of the same frequency
        nodePermutations = []
        for frequency in self.nodeMap:
            if len(self.nodeMap[frequency]) > 1:
                nodePermutations += list(itertools.permutations(self.nodeMap[frequency], 2))

        antiNodes = []

        for startAntenna, endAntenna in nodePermutations:
            end = endAntenna.position
            difference = end - startAntenna.position

            # keep moving the antinode along until it ends up out of bounds
            while self.nodeGrid.coordsInBounds(end):
                # only test unique positions
                if end not in antiNodes:
                    antiNodes.append(end)
                end += difference

        return len(antiNodes)


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
