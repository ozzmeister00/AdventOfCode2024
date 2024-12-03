"""
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock!
You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North
Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted.
All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions
like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to
 get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored,
 even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions.
 Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions.
What do you get if you add up all of the results of the multiplications?

--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact.
 If you handle some of the uncorrupted conditional statements in the program,
 you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8)
instructions are disabled because there is a don't() instruction before them. The other mul instructions
function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""
import logging
import os
import sys

import solver.runner
import solver.solver

import utils.logging
import utils.progress

logger = utils.logging.getLogger("day03", os.path.split(__file__)[0], level=logging.INFO, doStreamOutput=True)


class Instruction(object):
    """
    Base class for parser instructions
    """
    def __init__(self, functionName:str, *args):
        """

        :param functionName: how to identify the function, eg "mul"
        :param arg: list out the classes used as arguments for this function, eg. int, int
        """
        self.name = functionName
        self.arguments = args

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("You need to implement the call function otherwise the instruction won't work")

    @staticmethod
    def parse(index: int, blob: str) -> object:
        """
        :param index: where to start looking in the blob
        :param blob: the blob of instructions
        :return object: a valid instruction object if found, otherwise integer
        """
        raise NotImplementedError("You need to implement the parse function, otherwise the instruction won't compile")


class Mul(Instruction):
    """
    Implements the multiplication function
    """

    @staticmethod
    def parse(index: int, blob: str) -> object:
        # start parsing the instruction for the expected signature
        j = index + 3

        # if the next character after the string isn't an operen then skip it
        if blob[j] != "(":
            i = j
        else:

            # start looking for the first arguemnt
            j += 1
            firstArgument = ""

            # if the next character after the operen isn't numeric, bail out
            if not str.isnumeric(blob[j]):
                i = j + 1

            # now find all the digits up to the next comma
            while j < len(blob) and str.isnumeric(blob[j]):
                firstArgument += blob[j]
                j += 1

            # if the next character is a comma, we can proceed
            if blob[j] == ',':
                j += 1
                secondArgument = ""
                while j < len(blob) and str.isnumeric(blob[j]):
                    secondArgument += blob[j]
                    j += 1

                # if we found a cloperen at the end of the second argument, we're in good shape
                if blob[j] == ")":
                    newInstruction = Mul(int(firstArgument), int(secondArgument))

                    # final safety check
                    assert (str(newInstruction) in blob)

                    return newInstruction

            return j

    def __init__(self, A, B):
        super(Mul, self).__init__("mul", int, int)
        self.A = A
        self.B = B

    def __call__(self) -> int:
        return self.A * self.B

    def __repr__(self) -> str:
        return f"{self.name}({self.A},{self.B})"

    def __str__(self) -> str:
        return self.__repr__()


class Do(Instruction):
    @staticmethod
    def parse(index: int, blob: str) -> object:
        j = index + 2
        if blob[j] == "(":
            j += 1
            if blob[j] == ")":
                return Do()

        return j

    def __init__(self):
        super(Do, self).__init__("do")


class Dont(Instruction):
    @staticmethod
    def parse(index: int, blob: str) -> object:
        j = index + 5
        if blob[j] == "(":
            j += 1
            if blob[j] == ")":
                return Dont()

        return j

    def __init__(self):
        super(Dont, self).__init__("don't")


class Parser(object):
    """
    Parses input string of instructions into useful instructions
    """
    INSTRUCTIONS = {
        "mul": Mul,
        "do": Do,
        "don't": Dont
    }

    def __init__(self, instructionBlob:str):
        self.blob = instructionBlob
        self.instructions = []

        i = 0
        while i < len(self.blob) - 3:
            logger.debug(f"Looking for instruction at {i}")
            # check to see if this character, plus the next three are in the list of instructions
            for instructionName in Parser.INSTRUCTIONS:
                nextBit = self.blob[i:i + len(instructionName)]
                if nextBit == instructionName:
                    result = Parser.INSTRUCTIONS[instructionName].parse(i, self.blob)
                    if isinstance(result, Instruction):
                        logger.info(f"Found instruction {result.name}")
                        self.instructions.append(result)
                        i += len(instructionName) - 1

            # then move the pointer forward by one
            i += 1


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__(3, rawData=rawData)

    def ProcessInput(self) -> Parser:
        """
        Processes the stored raw data into self.processed

        :returns Parser:
        """
        return Parser(self.rawData)

    def SolvePartOne(self) -> int:
        """

        :returns the sum of multiplications of valid instructions:
        """
        result = 0
        logger.info(f"Solving Part 1 with number of instructions = {len(self.processed.instructions)}")
        for instruction in self.processed.instructions:
            if isinstance(instruction, Mul):
                result += instruction()

        return result

    def SolvePartTwo(self) -> int:
        """

        :return: the sum of enabled multiplications
        """
        result = 0
        do = True
        for instruction in self.processed.instructions:
            if isinstance(instruction, Do):
                do = True
            if isinstance(instruction, Dont):
                do = False
            if isinstance(instruction, Mul) and do:
                result += instruction()

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()

