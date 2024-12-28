"""
--- Day 12: Garden Groups ---
Why not search for the Chief Historian near the gardener and his massive farm? 
There's plenty of food, so The Historians grab something to eat while they 
search.

You're about to settle near a complex arrangement of garden plots when some 
Elves ask if you can lend a hand. They'd like to set up fences around each 
region of garden plots, but they can't figure out how much fence they need to 
order or how much it will cost. They hand you a map (your puzzle input) of the 
garden plots.

Each garden plot grows only a single type of plant and is indicated by a single 
letter on your map. When multiple garden plots are growing the same type of 
plant and are touching (horizontally or vertically), they form a region. For 
example:

AAAA
BBCD
BBCC
EEEC
This 4x4 arrangement includes garden plots growing five different types of 
plants (labeled A, B, C, D, and E), each grouped into their own region.

In order to accurately calculate the cost of the fence around a single region, 
you need to know that region's area and perimeter.

The area of a region is simply the number of garden plots the region contains. 
The above map's type A, B, and C plants are each in a region of area 4. The type
 E plants are in a region of area 3; the type D plants are in a region of area 
1.

Each garden plot is a square and so has four sides. The perimeter of a region is
 the number of sides of garden plots in the region that do not touch another 
garden plot in the same region. The type A and C plants are each in a region 
with perimeter 10. The type B and E plants are each in a region with perimeter 
8. The lone D plot forms its own region with perimeter 4.

Visually indicating the sides of plots in each region that contribute to the 
perimeter using - and |, the above map's regions' perimeters are measured as 
follows:

+-+-+-+-+
|A A A A|
+-+-+-+-+     +-+
              |D|
+-+-+   +-+   +-+
|B B|   |C|
+   +   + +-+
|B B|   |C C|
+-+-+   +-+ +
          |C|
+-+-+-+   +-+
|E E E|
+-+-+-+
Plants of the same type can appear in multiple separate regions, and regions can
 even appear within other regions. For example:

OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
The above map contains five regions, one containing all of the O garden plots, 
and the other four each containing a single X plot.

The four X regions each have area 1 and perimeter 4. The region containing 21 
type O plants is more complicated; in addition to its outer edge contributing a 
perimeter of 20, its boundary with each X region contributes an additional 4 to 
its perimeter, for a total perimeter of 36.

Due to "modern" business practices, the price of fence required for a region is 
found by multiplying that region's area by its perimeter. The total price of 
fencing all regions on a map is found by adding together the price of fence for 
every region on the map.

In the first example, region A has price 4 * 10 = 40, region B has price 4 * 8 =
 32, region C has price 4 * 10 = 40, region D has price 1 * 4 = 4, and region E 
has price 3 * 8 = 24. So, the total price for the first example is 140.

In the second example, the region with all of the O plants has price 21 * 36 = 
756, and each of the four smaller X regions has price 1 * 4 = 4, for a total 
price of 772 (756 + 4 + 4 + 4 + 4).

Here's a larger example:

RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
It contains:

A region of R plants with price 12 * 18 = 216.
A region of I plants with price 4 * 8 = 32.
A region of C plants with price 14 * 28 = 392.
A region of F plants with price 10 * 18 = 180.
A region of V plants with price 13 * 20 = 260.
A region of J plants with price 11 * 20 = 220.
A region of C plants with price 1 * 4 = 4.
A region of E plants with price 13 * 18 = 234.
A region of I plants with price 14 * 22 = 308.
A region of M plants with price 5 * 12 = 60.
A region of S plants with price 3 * 8 = 24.
So, it has a total price of 1930.

What is the total price of fencing all regions on your map?
"""
import collections 

import solver.runner
import solver.solver

import utils.math


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__(12, rawData=rawData)
        self.regions = []

    def ProcessInput(self) -> utils.math.Grid2D:
        """
        :returns: the map processed into a grid
        """
        width = len(self.rawData.split('\n')[0])
        return utils.math.Grid2D(width, data=self.rawData.replace('\n', ''))

    def checkNeighbors(self, coord: utils.math.Int2, region: list[utils.math.Int2], grid: utils.math.Grid2D) -> list[utils.math.Int2]:
        """
        Checks to see if the neighbors of the current coordinate match, and builds them into that region
        """
        region.append(coord)

        for neighborCoord, value in grid.enumerateOrthoLocalNeighbors(coord):
            if neighborCoord not in region and value == grid[coord]:
                region = self.checkNeighbors(neighborCoord, region, grid)

        return region

    def buildRegions(self, grid: utils.math.Grid2D) -> list[list[utils.math.Int2]]:
        """
        Look through all the coordinates in the grid and build a region
        from that coordinate. If the coordinate has already been marked
        as part of a region, skip it
        """
        regioned = []
        regions = []
        index = 0
        while len(regioned) < len(grid) and index < len(grid):
            coord = grid.indexToCoords(index)
            if coord not in regioned:
                region = self.checkNeighbors(coord, [], grid)
                regions.append(region)
                regioned += region

            index += 1

        return regions

    def scoreRegion(self, region: list[utils.math.Int2]) -> int:
        """
        Determines the area and perimeter of a region and returns
        the product of the two
        """
        area = len(region)
        perimeter = 0
        for coord in region:
            for direction in utils.math.Grid2D.orthoNeighbors:
                neighbor = coord + direction
                if neighbor not in region:
                    perimeter += 1
        
        return area * perimeter

    def SolvePartOne(self) -> int:
        """
        :return int: the total cost of fencing for the different plots in the farm
        """
        self.regions = self.buildRegions(self.processed)
        score = 0
        for region in self.regions:
            score += self.scoreRegion(region)

        return score

    def findPerimeterCoordsForRegion(self, region: list[utils.math.Int2]) -> list[utils.math.Int2]:
        """
        """
        value = self.processed[region[0]]
        
        # find all the coords by testing its neighbors, if any of the neighbors
        # of any given coordinate are NOT the same value as this region, 
        # then we know that given coordinate is on the perimeter of the region
        perimeterCoords = []
        for coord in region:
            neighborIndex = 0
            while neighborIndex < 4:
                neighbor = coord + utils.math.Grid2D.orthoNeighbors[neighborIndex]
                if self.processed.coordsInBounds(neighbor):
                    if self.processed[neighbor] != value:
                        perimeterCoords.append(coord)
                
                # if the coordinate is out of bounds, then we know this coordinate is on the perimeter!
                else:
                    perimeterCoords.append(coord)

                neighborIndex += 1

        return perimeterCoords

    def sortCoordinatesByConnection(self, startCoord: utils.math.Int2,\
                                          coordinates: list[utils.math.Int2],\
                                          sortedCoords: list[utils.math.Int2],\
                                          windingOrder: list[utils.math.Int2] = utils.math.Grid2D.clockwise) -> list[utils.math.Int2]:
        """
        Sorts the input list of coordinates by their connectedness starting from the
        first index of the input coordinates list in the input winding order
        """
        value = self.processed[startCoord]
        coordinates.pop(coordinates.index(startCoord))
        sortedCoords.append(startCoord)

        neighborIndex = 0
        while neighborIndex < 4 and coordinates:
            neighbor = startCoord + windingOrder[neighborIndex]
            if self.processed.coordsInBounds(neighbor):
                if neighbor in coordinates and neighbor not in sortedCoords:
                    neighborIndex = 4
                    sortedCoords = self.sortCoordinatesByConnection(neighbor, coordinates, sortedCoords, windingOrder=windingOrder)

            neighborIndex += 1

        return sortedCoords

    def checkBoundary(self, coordFacing: tuple[utils.math.Int2, utils.math.Int2], group: list[utils.math.Int2], coords: list[tuple[utils.math.Int2, utils.math.Int2]]) -> list[utils.math.Int2]:
        """
        Check to see which of the neighbors of the input coordinate are in the input
        list of coordinates and share a direction, and build out from there
        """
        coord, facing = coordFacing
        group.append(coordFacing)

        for direction in utils.math.Grid2D.orthoNeighbors:
            neighborCoord = coord + direction
            neighborFacing = (neighborCoord, facing)
            if neighborFacing in coords and neighborFacing not in group:
                group = self.checkBoundary(neighborFacing, group, coords)

        return group

    def buildCoordinateGroups(self, coords: list[utils.math.Grid2D]) -> list[list[utils.math.Int2]]:
        """
        Look through all the coordinates in the grid and build a region
        from that coordinate. If the coordinate has already been marked
        as part of a region, skip it
        """
        grouped = []
        groups = []
        index = 0
        while len(grouped) < len(coords) and index < len(coords):
            coordFacing = coords[index]
            if coordFacing not in grouped:
                group = self.checkBoundary(coordFacing, [], coords)
                groups.append(group)
                grouped += group

            index += 1

        return groups

    def getNumSidesOfRegion(self, region: list[utils.math.Int2]) -> int:
        """
        Finds the number of sides of the input region of points
        """
        value = self.processed[region[0]]

        perimeterCoords = self.findPerimeterCoordsForRegion(region)

        # once we have the list of perimeter coordinates, we need to find
        # all the coordinates (including those out of bounds of the grid)
        # that are reachable from the coordinates. We're in effect inflating the
        # perimeter coordinates. This should give us a number of discontiguous 
        # sets of coordinates outside the perimeter and we can find the total 
        # number of connected sets of coordinates to find the number of sides
        
        # we need to store the boundary coordinates AND the directions from which they were reached
        # since those are different "sides"
        boundaryCoords = []

        # loop over all the coordinates in the perimeter
        for perimeterCoord in perimeterCoords:
            # and all of the possible orthogonal directions
            for direction in utils.math.Grid2D.orthoNeighbors:
                coord = perimeterCoord + direction

                # if the coordinate is out of bounds of the grid, we know it's a boundary
                if not self.processed.coordsInBounds(coord):
                    boundaryCoords.append((coord, direction))

                # if the neighbor doesn't have the same value, we know that that direction is a boundary
                elif self.processed[coord] != value:
                    boundaryCoords.append((coord, direction))

        # then construct all the connected boundary coordinates into separate lists 
        boundaryEdges = self.buildCoordinateGroups(boundaryCoords)

        return len(boundaryEdges)

    def scoreRegionSides(self, region: list[utils.math.Int2]) -> int:
        """
        Figures out the number of SIDES the region has and multiplies 
        THAT by the area of the region to determine its cost
        """
        area = len(region)  

        numSides = self.getNumSidesOfRegion(region)

        return numSides * area

    def SolvePartTwo(self) -> int:
        """

        :return int: the cost of regions if the cost is equal to number of region sides * area
        """
        if not self.regions:
            self.regions = self.buildRegions(self.processed)

        score = 0
        for region in self.regions:
            score += self.scoreRegionSides(region)

        return score


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
