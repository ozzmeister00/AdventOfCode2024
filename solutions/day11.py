"""
--- Day 11: Plutonian Pebbles ---
The ancient civilization on Pluto was known for its ability to manipulate 
spacetime, and while The Historians explore their infinite corridors, you've 
noticed a strange set of physics-defying stones.

At first glance, they seem like normal stones: they're arranged in a perfectly 
straight line, and each stone has a number engraved on it.

The strange part is that every time you blink, the stones change.

Sometimes, the number engraved on a stone changes. Other times, a stone might 
split in two, causing all the other stones to shift over a bit to make room in 
their perfectly straight line.

As you observe them for a while, you find that the stones have a consistent 
behavior. Every time you blink, the stones each simultaneously change according 
to the first applicable rule in this list:

If the stone is engraved with the number 0, it is replaced by a stone engraved 
with the number 1.
If the stone is engraved with a number that has an even number of digits, it is 
replaced by two stones. The left half of the digits are engraved on the new left
 stone, and the right half of the digits are engraved on the new right stone. 
(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 
and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old 
stone's number multiplied by 2024 is engraved on the new stone.
No matter how the stones change, their order is preserved, and they stay on 
their perfectly straight line.

How will the stones evolve if you keep blinking at them? You take a note of the 
number engraved on each stone in the line (your puzzle input).

If you have an arrangement of five stones engraved with the numbers 0 1 10 99 
999 and you blink once, the stones transform as follows:

The first stone, 0, becomes a stone marked 1.
The second stone, 1, is multiplied by 2024 to become 2024.
The third stone, 10, is split into a stone marked 1 followed by a stone marked 
0.
The fourth stone, 99, is split into two stones marked 9.
The fifth stone, 999, is replaced by a stone marked 2021976.
So, after blinking once, your five stones would become an arrangement of seven 
stones engraved with the numbers 1 2024 1 0 9 9 2021976.

Here is a longer example:

Initial arrangement:
125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
In this example, after blinking six times, you would have 22 stones. After 
blinking 25 times, you would have 55312 stones!

Consider the arrangement of stones in front of you. How many stones will you 
have after blinking 25 times?
"""
import functools
import math
import time

import solver.runner
import solver.solver


class StoneEvolutionRule(object):
    NAME = "BASE"
    
    def isValid(self, stoneID: int) -> bool:
        raise NotImplementedError("Rule needs to implement isValid to see if a stone matches the rule")
    
    def resolve(self, stoneID: int) -> list[int]:
        raise NotImplementedError("Rule needs to implement a resolve so that the stone's ID is correctly resolved")


class Zero(StoneEvolutionRule):
    NAME = "Zero"

    def __init__(self):
        super(Zero, self).__init__()

    def isValid(self, stoneID: int) -> bool:
        return stoneID == 0

    def resolve(self, stoneID: int) -> list[int]:
        return 1


class EvenNumDigits(StoneEvolutionRule):
    NAME = "EvenNumDigits"

    def __init__(self):
        super(EvenNumDigits, self).__init__()
        self.numDigits = 0

    def isValid(self, stoneID: int) -> bool:
        self.numDigits = int(math.log10(stoneID)+1)
        return self.numDigits % 2 == 0

    def resolve(self, stoneID: int) -> list[int]:
        splitPoint = 10 ** (self.numDigits / 2)
        shifted = stoneID / splitPoint
        left = int(shifted)
        # round this because the frac stuff might cause floating point issues
        right = round((shifted - left) * splitPoint)
        return [left, right]


class Default(StoneEvolutionRule):
    NAME = "Default"

    def __init__(self):
        super(Default, self).__init__()

    def isValid(self, stoneID: int) -> bool:
        return True

    def resolve(self, stoneID: int) -> int:
        return stoneID * 2024


ZERO = Zero()
EVENNUMDIGITS = EvenNumDigits()
DEFAULT = Default()


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__(11, rawData=rawData)
        self.partOneStones = []

    def ProcessInput(self) -> list[int]:
        """
        :returns: an array of integers representing the inital state of the stones
        """
        return list(map(int, self.rawData.split(' ')))

    @functools.cache
    def resolveStone(self, stoneID: int, times: int) -> int:
        """
        Checks all the rules that could apply to this stone and
        apply the most appropriate one, returning the resulting stone(s)
        """
        if times == 0:
            return 1

        if ZERO.isValid(stoneID):
            return self.resolveStone(ZERO.resolve(stoneID), times - 1)
        elif EVENNUMDIGITS.isValid(stoneID):
            left, right = EVENNUMDIGITS.resolve(stoneID)
            return self.resolveStone(left, times - 1) + self.resolveStone(right, times - 1)

        return self.resolveStone(DEFAULT.resolve(stoneID), times - 1)

    def SolvePartOne(self) -> int:
        """

        :return int: the number of stones after 25 blinks
        """
        result = 0
        times = 25
        for stoneID in self.processed:
            result += self.resolveStone(stoneID, times)

        return result

    def SolvePartTwo(self) -> int:
        """

        :return int: the result
        """
        result = 0
        times = 75
        for stoneID in self.processed:
            result += self.resolveStone(stoneID, times)

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
