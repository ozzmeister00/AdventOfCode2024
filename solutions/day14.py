"""
--- Day 14: Restroom Redoubt ---
One of The Historians needs to use the bathroom; fortunately, you know there's a
 bathroom near an unvisited location on their list, and so you're all quickly 
teleported directly to the lobby of Easter Bunny Headquarters.

Unfortunately, EBHQ seems to have "improved" bathroom security again after your 
last visit. The area outside the bathroom is swarming with robots!

To get The Historian safely to the bathroom, you'll need a way to predict where 
the robots will be in the future. Fortunately, they all seem to be moving on the
 tile floor in predictable straight lines.

You make a list (your puzzle input) of all of the robots' current positions (p) 
and velocities (v), one robot per line. For example:

p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
Each robot's position is given as p=x,y where x represents the number of tiles 
the robot is from the left wall and y represents the number of tiles from the 
top wall (when viewed from above). So, a position of p=0,0 means the robot is 
all the way in the top-left corner.

Each robot's velocity is given as v=x,y where x and y are given in tiles per 
second. Positive x means the robot is moving to the right, and positive y means 
the robot is moving down. So, a velocity of v=1,-2 means that each second, the 
robot moves 1 tile to the right and 2 tiles up.

The robots outside the actual bathroom are in a space which is 101 tiles wide 
and 103 tiles tall (when viewed from above). However, in this example, the 
robots are in a space which is only 11 tiles wide and 7 tiles tall.

The robots are good at navigating over/under each other (due to a combination of
 springs, extendable legs, and quadcopters), so they can share the same tile and
 don't interact with each other. Visually, the number of robots on each tile in 
this example looks like this:

1.12.......
...........
...........
......11.11
1.1........
.........1.
.......1...
These robots have a unique feature for maximum bathroom security: they can 
teleport. When a robot would run into an edge of the space they're in, they 
instead teleport to the other side, effectively wrapping around the edges. Here 
is what robot p=2,4 v=2,-3 does for the first few seconds:

Initial state:
...........
...........
...........
...........
..1........
...........
...........

After 1 second:
...........
....1......
...........
...........
...........
...........
...........

After 2 seconds:
...........
...........
...........
...........
...........
......1....
...........

After 3 seconds:
...........
...........
........1..
...........
...........
...........
...........

After 4 seconds:
...........
...........
...........
...........
...........
...........
..........1

After 5 seconds:
...........
...........
...........
.1.........
...........
...........
...........
The Historian can't wait much longer, so you don't have to simulate the robots 
for very long. Where will the robots be after 100 seconds?

In the above example, the number of robots on each tile after 100 seconds has 
elapsed looks like this:

......2..1.
...........
1..........
.11........
.....1.....
...12......
.1....1....
To determine the safest area, count the number of robots in each quadrant after 
100 seconds. Robots that are exactly in the middle (horizontally or vertically) 
don't count as being in any quadrant, so the only relevant robots are:

..... 2..1.
..... .....
1.... .....

..... .....
...12 .....
.1... 1....
In this example, the quadrants contain 1, 3, 4, and 1 robot. Multiplying these 
together gives a total safety factor of 12.

Predict the motion of the robots in your list within a space which is 101 tiles 
wide and 103 tiles tall. What will the safety factor be after exactly 100 
seconds have elapsed?
"""
import os
import re

import PIL

import solver.runner
import solver.solver

import utils.constants
import utils.math
import utils.logging

logger = utils.logging.getLogger("day14", utils.constants.getOutputsFolder(), doStreamOutput=True)


class Robot(object):
    REGEX = '((?:\d+|-\d+)+)'

    def __init__(self, position: utils.math.Int2, velocity: utils.math.Int2):
        self.startPosition = position
        self.position = position
        self.velocity = velocity

    def advance(self, n: int, gridSize=utils.math.Int2(1, 1)) -> utils.math.Int2:
        """
        Advance the robot N seconds in the direction of its velocity, filterign its resulting position
        by the width and height
        """
        self.position += self.velocity * n 
        self.position %= gridSize
        return self.position 

    def reset(self):
        self.position = self.startPosition

    @staticmethod
    def fromString(inString: str):
        px, py, vx, vy = re.findall(Robot.REGEX, inString)
        return Robot(utils.math.Int2(px, py), utils.math.Int2(vx, vy))


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None, width=101, height=103):
        super(Solver, self).__init__(14, rawData=rawData)
        self.width = width
        self.height = height
        self.size = utils.math.Int2(self.width, self.height)

    def ProcessInput(self) -> list[Robot]:
        """
        :returns: the list of robots from the input data
        """
        return [Robot.fromString(inString) for inString in self.rawData.split('\n')]

    def SolvePartOne(self) -> int:
        """
        :return int: the product of the number of robots in each quadrant after 100 seconds
        """
        # advance all the robots 100 times and get their resulting positions
        resultingPositions = [r.advance(100, gridSize=self.size) for r in self.processed]

        # then make four bounding boxes for each quadrant
        zero = utils.math.Int2()
        midpoint = self.size / 2
        topLeft = utils.math.BoundingBox2D(zero, midpoint)
        topRight = utils.math.BoundingBox2D(utils.math.Int2(midpoint.x + 1, 0), utils.math.Int2(self.width + 1, midpoint.y))
        bottomLeft = utils.math.BoundingBox2D(utils.math.Int2(0, midpoint.y + 1), utils.math.Int2(midpoint.x, self.height + 1))
        bottomRight = utils.math.BoundingBox2D(midpoint + 1, self.size + 1)

        bboxes = [topLeft, topRight, bottomLeft, bottomRight]
        result = 1
        for bbox in bboxes:
            quadrantScore = 0
            for filtered in resultingPositions:
                if bbox.pointInside(filtered):
                    quadrantScore += 1
            
            result *= quadrantScore

        return result

    def SolvePartTwo(self) -> int:
        """
        :return int: the number of seconds that elapsed before the pattern resulted in a Christmas Tree
        """
        result = 0

        # create a grid so we can draw the result
        grid = utils.math.Grid2D(self.width, data=' ' * self.width * self.height)

        # rewind the robots to their starting positions
        for r in self.processed:
            r.reset()

        seconds = 0

        while input('Proceed? Y/N> ') == 'Y':
            # clear the grid bufffer between attempts
            for i, v in enumerate(grid):
                grid[i] = ' '

            newPositions = [r.advance(1, gridSize=self.size) for r in self.processed]

            # then draw those positions to the grid
            for p in newPositions:
                grid[p] = '#'

            with open(os.path.join(utils.constants.getOutputsFolder(), f'{seconds}.txt'), 'w') as fh:
                fh.write(str(grid))

            seconds += 1

        return seconds


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
