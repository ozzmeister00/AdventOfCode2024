"""
--- Day 15: Warehouse Woes ---
You appear back inside your own mini submarine! Each Historian drives their mini
 submarine in a different direction; maybe the Chief has his own submarine down 
here somewhere as well?

You look up to see a vast school of lanternfish swimming past you. On closer 
inspection, they seem quite anxious, so you drive your mini submarine over to 
see if you can help.

Because lanternfish populations grow rapidly, they need a lot of food, and that 
food needs to be stored somewhere. That's why these lanternfish have built 
elaborate warehouse complexes operated by robots!

These lanternfish seem so anxious because they have lost control of the robot 
that operates one of their most important warehouses! It is currently running 
amok, pushing around boxes in the warehouse with no regard for lanternfish 
logistics or lanternfish inventory management strategies.

Right now, none of the lanternfish are brave enough to swim up to an 
unpredictable robot so they could shut it off. However, if you could anticipate 
the robot's movements, maybe they could find a safe option.

The lanternfish already have a map of the warehouse and a list of movements the 
robot will attempt to make (your puzzle input). The problem is that the 
movements will sometimes fail as boxes are shifted around, making the actual 
movements of the robot difficult to predict.

For example:

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
As the robot (@) attempts to move, if there are any boxes (O) in the way, the 
robot will also attempt to push those boxes. However, if this action would cause
 the robot or a box to move into a wall (#), nothing moves instead, including 
the robot. The initial positions of these are shown on the map at the top of the
 document the lanternfish gave you.

The rest of the document describes the moves (^ for up, v for down, < for left, 
> for right) that the robot will attempt to make, in order. (The moves form a 
single giant sequence; they are broken into multiple lines just to make copy-
pasting easier. Newlines within the move sequence should be ignored.)

Here is a smaller example to get started:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
Were the robot to attempt the given sequence of moves, it would push around the 
boxes as follows:

Initial state:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move <:
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move ^:
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move >:
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########

Move >:
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########

Move v:
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########

Move <:
########
#....OO#
##.....#
#.....O# 
#.#O@..#
#...O..#
#...O..#
########
The larger example has many more moves; after the robot has finished those 
moves, the warehouse would look like this:

##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
The lanternfish use their own custom Goods Positioning System (GPS for short) to
 track the locations of the boxes. The GPS coordinate of a box is equal to 100 
times its distance from the top edge of the map plus its distance from the left 
edge of the map. (This process does not stop at wall tiles; measure all the way 
to the edges of the map.)

So, the box shown below has a distance of 1 from the top edge of the map and 4 
from the left edge of the map, resulting in a GPS coordinate of 100 * 1 + 4 = 
104.

#######
#...O..
#......
The lanternfish would like to know the sum of all boxes' GPS coordinates after 
the robot finishes moving. In the larger example, the sum of all boxes' GPS 
coordinates is 10092. In the smaller example, the sum is 2028.

Predict the motion of the robot and boxes in the warehouse. After the robot is 
finished moving, what is the sum of all boxes' GPS coordinates?
"""
import collections
import re

import solver.runner
import solver.solver

import utils.math


MOVES = {'^': utils.math.Grid2D.South,
         '<': utils.math.Grid2D.West,
         '>': utils.math.Grid2D.East,
         'v': utils.math.Grid2D.North}


class Actor(object):
    ICON = 'X'

    def __init__(self, position: utils.math.Int2):
        self.position = position
    
    def canMove(self) -> bool:
        """
        Whether or not the object can be moved
        """
        return False

    def isEmpty(self) -> bool:
        return False

    def  gpsCoordinateScore(self) -> int:
        return (self.position.y * 100) + self.position.x

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.position})'

    def __str__(self) -> str:
        return self.__class__.ICON


class Wall(Actor):
    ICON = '#'

class Robot(Actor):
    ICON = '@'

class Box(Actor):
    ICON = 'O'

    def canMove(self) -> bool:
        return True

class Empty(Actor):
    ICON = '.'

    def isEmpty(self) -> bool:
        return True


class MapDisplay(utils.math.Grid2D):
    def clear(self):
        for i, v in enumerate(self):
            self[i] = '.'

    def updateActors(self, actors: list[Actor]):
        for a in actors:
            if not a.isEmpty():
                self[a.position] = a.ICON


ACTOR_MAPPING = {Wall.ICON: Wall,
                 Box.ICON: Box}

INSTRUCITON_REGEX = '([\^|\<|\>|v]+)'
ACTOR_REGEX = '([#|\.|O|@]+)'

class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        self.instructionSet = []

        # store all our actors in a dictionary mapping to their positions
        self.actors = collections.defaultdict(utils.math.Int2)

        # store the robot separately so we know we can get at it at all times
        self.robot = Robot(utils.math.Int2())

        # and set up a variable for a display map that we can draw to when needed
        self.mapDisplay = None

        super(Solver, self).__init__(15, rawData=rawData)

    def ProcessInput(self):
        """
        :returns: take the input and stash off the instructions into an array, and the actors' initial positions
        into a dictionary mapping their locations to the actor itself
        """
        # collapse the instruction set down into a single line
        self.instructionSet = ''.join(re.findall(INSTRUCITON_REGEX, self.rawData))

        # create a quick and dirty grid so we can get the coordinates of the actors
        actors = ''.join(re.findall(ACTOR_REGEX, self.rawData))
        width = len(self.rawData.splitlines()[0])
        self.mapDisplay = MapDisplay(width, actors)

        # find the coordinates of the robot first
        self.robot.position = self.mapDisplay.findCoords(Robot.ICON)[0]

        # then populate the actor dict with the appropriate actors
        for coord, value in self.mapDisplay.enumerateCoords():
            if value in ACTOR_MAPPING:
                self.actors[coord] = ACTOR_MAPPING[value](coord)

        # be sure to clear the display map so we have a clean slate to draw to
        self.mapDisplay.clear()

    def SolvePartOne(self) -> int:
        """
        :return int: the sum of all boxes' GPS coordinates (100 * X + Y) 
        after the Robot's instructions have been run
        """
        maxDistance = utils.math.Int2(self.mapDisplay.width, self.mapDisplay.height)

        for instruction in self.instructionSet:
            direction = MOVES[instruction]

            # keep the trace in-bounds
            traceEnd = self.robot.position + (maxDistance * direction)
            traceEnd.x = utils.math.clamp(traceEnd.x, 0, maxDistance.x)
            traceEnd.y = utils.math.clamp(traceEnd.y, 0, maxDistance.y)

            line = utils.math.Line2D(self.robot.position + direction, traceEnd)
            traceHits = [self.actors[coord] if coord in self.actors else Empty(coord) for coord in line.getIntegerPoints()]
            
            # if we aren't at the edge of the map, then we can probably do something
            if traceHits:
                # if there's nothing in front of us, we can easily move there
                if traceHits[0].isEmpty():
                    self.robot.position += direction
                # otherwise, we gotta do some work
                else:
                    # if we can't move, don't do anything else
                    if not traceHits[0].canMove():
                        pass
                    # if the first thing we hit can move, the real work begins
                    else:
                        # find the last index at which there are movable and non-empty actors
                        index = 0
                        while index < len(traceHits) and traceHits[index].canMove() and not traceHits[index].isEmpty():
                            index += 1

                        # if the next space is empty, then we need to move all the actors to new locations
                        if traceHits[index].isEmpty():
                            # first, blank out the mapping of coords to actors
                            currentCoordinates = [a.position for a in traceHits[:index]]
                            
                            # empty out the cache for the given actor positions
                            for coord in currentCoordinates:
                                self.actors[coord] = Empty(coord)
                            
                            # then we can put the actors in their new coordinates
                            for a in traceHits[:index]:
                                a.position += direction      
                                self.actors[a.position] = a
                            
                            # finally, scoot the robot in the move diretion
                            self.robot.position += direction

            self.mapDisplay.clear()
            self.mapDisplay.updateActors([self.robot] + list(self.actors.values()))

        # after all is said and done, total up the box's GPS coordinates
        return sum([a.gpsCoordinateScore() for a in self.actors.values() if isinstance(a, Box)])

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
