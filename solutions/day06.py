"""
Day06
"""

import solver.runner
import solver.solver

import utils.math

INITIAL_GUARD_CHARACTER = '^'
OBSTRUCTION = '#'
VISITED = 'X'


class Guard(object):
    """
    A little class to make it easy to represent the guard in the grid
    """

    FACING = {utils.math.Grid2D.South: '^',
              utils.math.Grid2D.West: '<',
              utils.math.Grid2D.North: 'v',
              utils.math.Grid2D.East: '>',
              }

    def __init__(self, position: utils.math.Int2, direction: utils.math.Int2):
        self.position = position
        self.direction = direction

    def __str__(self):
        return Guard.FACING[self.direction]


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        # initialize values we'll access later
        self.grid = None
        self.guard = None

        super(Solver, self).__init__(6, rawData=rawData)

    def ProcessInput(self) -> None:
        """
        Turn the input into a 2D grid, then find the position of the guard
        and stash them in the grid
        """
        width = len(self.rawData.splitlines()[0])
        rawData = self.rawData.replace('\n', '')

        self.grid = utils.math.Grid2D(width, data=rawData)
        indexes = self.grid.findIndexes(INITIAL_GUARD_CHARACTER)
        assert(len(indexes) == 1)

        # then store the guard off as its own object that we'll keep track of
        # "South" in my coordinate space is "Up" if you're looking at the input data
        # TODO 2024_12_08 one day I'll have to transpose all this stuff so that it's drawn properly
        # TODO but interpreted without me having to do a bunch of mental gymnastics
        self.guard = Guard(self.grid.indexToCoords(indexes[0]), self.grid.South)

    def plotGuardsPath(self):
        """
        Resolve the guard's path until they leave the area

        If there is something direcly in front of you, turn right 90 degrees
        otherwise, keep walking
        """
        directionIndex = 0
        clockwise = [self.grid.South, self.grid.Right, self.grid.Up, self.grid.Left]

        # while the guard's position is in bounds of the grid
        while self.grid.coordsInBounds(self.guard.position):
            self.grid[self.guard.position] = VISITED

            # brute force would have us advance the guard's position once each cycle
            # but we're evolved creatures, and that's just silly, so instead
            # grab the line from in front of the guard to the edge of the map
            start = self.guard.position + self.guard.direction

            end = utils.math.Int2(self.guard.position.x, self.guard.position.y)

            # explicitly target the edge of the grid
            if self.guard.direction.x < 0:
                end.x = 0
            elif self.guard.direction.x > 0:
                end.x = self.grid.width - 1

            if self.guard.direction.y < 0:
                end.y = 0
            elif self.guard.direction.y > 0:
                end.y = self.grid.height - 1

            path = utils.math.Line2D(start, end)
            pathItems = self.grid[path]
            if OBSTRUCTION in pathItems:
                # figure out where the first obstruction is
                firstObstruction = pathItems.index(OBSTRUCTION) - 1

                # then move the end point there, less one
                end = start + (self.guard.direction * firstObstruction)

                path = utils.math.Line2D(start, end)

                # finally, update the guard's position and direction
                directionIndex += 1
                directionIndex %= len(clockwise)

                self.guard.position = end
                self.guard.direction = clockwise[directionIndex]
            # if we don't find any obstructions, then we can move the guard out of bounds
            else:
                self.guard.position = end + self.guard.direction

            # finally, mark all the points in the path as visited
            for coord in path.getIntegerPoints():
                self.grid[coord] = VISITED

    def SolvePartOne(self) -> int:
        """
        :return int: the number of distinct positions the guard visits on the map
        """
        # plot the guard's path using the known rules
        self.plotGuardsPath()

        # then get the number of visited locations
        return self.grid.count(VISITED)

    def SolvePartTwo(self) -> int:
        """
        :return int: the number of positions that could contain an obstruction which would cause the guard's path to loop
        """
        result = 0

        # maybe we ARE merely mortal, and brute forcing is the only true path?
        # at the very least we can bound our search to all the spots the guard visits on a single loop
        # BUT in order to detect that the path is cyclical, we can't rely on the assumption that the guard
        # will exit the loop (and thus the While loop gets... hairy)

        # so in order to MARGINALLY efficient about our brute force we need to:
        # 1. Have a way to detect if the guard ends up in a loop
        # 2. Place on obstruction on all the places the guard visits with the exception of the starting position
        #    and re-run the simulation, counting all the variants in which the guard ends up in an infinite loop

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
