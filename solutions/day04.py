"""
"Looks like the Chief's not here. Next!" One of The Historians pulls out a 
device and pushes the only button on it.
After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs
 on your shirt; she'd like to know
if you could help her with her word search (your puzzle input). She only has to 
find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written 
backwards, or even overlapping other words.
 It's a little unusual, though, as you don't merely need to find one instance of
 XMAS - you need to find all of them.
 Here are a few ways XMAS might appear, where irrelevant characters have been 
replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word 
search again,
but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?
"""

import utils.math

import solver.runner
import solver.solver

# cache off XMAS as a list
# since we're going to pull it from the grid as a list, it'll be faster to compare list to list
# than anything else
XMAS = ['X', 'M', 'A', 'S']


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__(4, rawData=rawData)

    def ProcessInput(self) -> utils.math.Grid2D:
        """
        :returns utils.math.Grid2D: the input parsed into a grid
        """
        width = len(self.rawData.splitlines()[0])
        rawData = self.rawData.replace('\n', '')

        return utils.math.Grid2D(width, rawData)

    def findXMasInDirection(self, coord: utils.math.Int2, direction: utils.math.Int2) -> bool:
        """
        Searches in one direction for XMAS

        :param coord: the coordinate to start from
        :param direction: the direction to search in
        :return bool: if we've found XMAS
        """
        endPoint = coord + direction * 3
        if self.processed.coordsInBounds(endPoint):
            section = self.processed[coord:endPoint]
            return section == XMAS

        return False

    def findXMas(self, coord: utils.math.Int2) -> int:
        """
        Searches in all directions for Xmas from the input coordinate
        :return int: number of XMASes found at this coordinate"""
        found = 0

        for direction in utils.math.Grid2D.neighbors:
            if self.findXMasInDirection(coord, direction):
                found += 1

        return found

    def SolvePartOne(self) -> int:
        """
        :return int: the number of times XMAS appears in the input grid
        """
        result = 0

        # first, find the coords of all the Xs, since we know that XMAS can only start at X
        xCoords = self.processed.findCoords('X')
        for x in xCoords:
            result += self.findXMas(x)

        return result

    def isCoordMAS(self, coord: utils.math.Int2) -> bool:
        """
        check the corners surrounding the input coordinate to see if
        they're S and then M or M and then S

        :param coord:
        :return: if an x-shaped MAS appears at this coordinate
        """
        sw = coord + utils.math.Grid2D.SouthWest
        nw = coord + utils.math.Grid2D.NorthWest
        ne = coord + utils.math.Grid2D.NorthEast
        se = coord + utils.math.Grid2D.SouthEast

        # if any of the coordinates are out of bounds,
        # bail out early because we know that couldn't possibly fit the criteria
        if not all([self.processed.coordsInBounds(x) for x in [sw, nw, ne, se]]):
            return False

        count = 0
        # if the SouthWest and NorthEast coordinates are S and M, or M and S, then we know we have one
        if (self.processed[sw] == 'S' and self.processed[ne] == 'M') or\
           (self.processed[sw] == 'M' and self.processed[ne] == 'S'):
            count += 1
        # then if the NorthWest and SouthEast coordinates are S and M, or M and S, then we know we have the other
        if (self.processed[nw] == 'S' and self.processed[se] == 'M') or\
             (self.processed[nw] == 'M' and self.processed[se] == 'S'):
            count += 1

        # and if we have both, we're golden!
        return count == 2

    def SolvePartTwo(self) -> int:
        """
        :return int: the number of MASes in the shape of an X
        """
        result = 0

        # first find all the A coordinates
        aCoords = self.processed.findCoords('A')

        for a in aCoords:
            if self.isCoordMAS(a):
                result += 1

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
