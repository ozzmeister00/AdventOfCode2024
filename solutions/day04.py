"""
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it.
After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know
if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words.
 It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them.
 Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


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
In this word search, XMAS occurs a total of 18 times; here's the same word search again,
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

XMAS = "XMAS"


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
        pass

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



        return result

    def SolvePartTwo(self):
        """

        :return int: the result
        """
        result = 0

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
