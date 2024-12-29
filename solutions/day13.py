"""
--- Day 13: Claw Contraption ---
Next up: the lobby of a resort on a tropical island. The Historians take a 
moment to admire the hexagonal floor tiles before spreading out.

Fortunately, it looks like the resort has a new arcade! Maybe you can win some 
prizes from the claw machines?

The claw machines here are a little unusual. Instead of a joystick or 
directional buttons to control the claw, these machines have two buttons labeled
 A and B. Worse, you can't just put in a token and play; it costs 3 tokens to 
push the A button and 1 token to push the B button.

With a little experimentation, you figure out that each machine's buttons are 
configured to move the claw a specific amount to the right (along the X axis) 
and a specific amount forward (along the Y axis) each time that button is 
pressed.

Each machine contains one prize; to win the prize, the claw must be positioned 
exactly above the prize on both the X and Y axes.

You wonder: what is the smallest number of tokens you would have to spend to win
 as many prizes as possible? You assemble a list of every machine's button 
behavior and prize location (your puzzle input). For example:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
This list describes the button configuration and prize location of four 
different claw machines.

For now, consider just the first claw machine in the list:

Pushing the machine's A button would move the claw 94 units along the X axis and
 34 units along the Y axis.
Pushing the B button would move the claw 22 units along the X axis and 67 units 
along the Y axis.
The prize is located at X=8400, Y=5400; this means that from the claw's initial 
position, it would need to move exactly 8400 units along the X axis and exactly 
5400 units along the Y axis to be perfectly aligned with the prize in this 
machine.
The cheapest way to win the prize is by pushing the A button 80 times and the B 
button 40 times. This would line up the claw along the X axis (because 80*94 + 
40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). Doing this 
would cost 80*3 tokens for the A presses and 40*1 for the B presses, a total of 
280 tokens.

For the second and fourth claw machines, there is no combination of A and B 
presses that will ever win a prize.

For the third claw machine, the cheapest way to win the prize is by pushing the 
A button 38 times and the B button 86 times. Doing this would cost a total of 
200 tokens.

So, the most prizes you could possibly win is two; the minimum tokens you would 
have to spend to win all (two) prizes is 480.

You estimate that each button would need to be pressed no more than 100 times to
 win a prize. How else would someone be expected to play?

Figure out how to win as many prizes as possible. What is the fewest tokens you 
would have to spend to win all possible prizes?
"""

import functools
import math
# let it be known that on this day, the 28th day of December in the 2,024th year of our lord
# I finally caved to use regex in Advent of Code
import re

import solver.runner
import solver.solver

import utils.math


class ClawMachine(object):
    """
    Object to store A button, B button, and prize coordinate
    of a given claw machine
    """
    def __init__(self, a: utils.math.Int2, b: utils.math.Int2, prize: utils.math.Int2):
        self.a = a 
        self.b = b
        self.prize = prize

    def getCheapestPath(self, partTwo = False) -> int:
        """
        Evaluates all the valid paths and returns the cheapest
        """
        prize = self.prize + 10000000000000 if partTwo else self.prize

        top = ((prize.x * self.b.y) - (self.b.x * prize.y))
        bottom = ((self.a.x * self.b.y) - (self.b.x * self.a.y))

        if top % bottom != 0:
            return 0

        a = top // bottom

        b = (prize.x - a * self.a.x) // self.b.x
        return 3 * a + b

    @staticmethod
    def fromString(inString: str):
        aLine, bLine, prizeLine = inString.split('\n')
        buttonRegex = 'X\+(\d*), Y\+(\d*)'
        a = utils.math.Int2(*re.findall(buttonRegex, aLine))
        b = utils.math.Int2(*re.findall(buttonRegex, bLine))
        prizeRegex = 'X\=(\d*), Y\=(\d*)'
        prize = utils.math.Int2(*re.findall(prizeRegex, prizeLine))

        return ClawMachine(a, b, prize)


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__(13, rawData=rawData)

    def ProcessInput(self) -> list[ClawMachine]:
        """
        :returns: a list of all the unique claw machines in the input data
        """
        clawMachineRegex = "((?:Button A: X\+\d*, Y\+\d*\nButton B: X\+\d*, Y\+\d*\nPrize: X=\d*, Y=\d+)+)"
        processed = []
        for section in re.findall(clawMachineRegex, self.rawData):
            processed.append(ClawMachine.fromString(section))

        return processed

    def SolvePartOne(self) -> int:
        """
        A costs 3
        B costs 1
        :return int: the fewest tokens needed to win all possible prizes
        """
        return sum([machine.getCheapestPath() for machine in self.processed])

    def SolvePartTwo(self) -> int:
        """
        :return int: the fewest tokens needed to win all possible prizes, with the new offset
        """
        return sum([machine.getCheapestPath(partTwo=True) for machine in self.processed])


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()

# 106371526647967 is WRONG