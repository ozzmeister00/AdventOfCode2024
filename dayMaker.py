'''
Script to automatically make the input, test, and solver files for a given day
'''

import argparse
import os
import sys

PROJECT_DIR = os.path.split(__file__)[0]

SOLVER_TEMPLATE_FILE = os.path.join(PROJECT_DIR, "templates", "template.py")
TEST_TEMPLATE_FILE = os.path.join(PROJECT_DIR, "templates", "test_template.py")
INPUT_DIR = os.path.join(PROJECT_DIR, "inputData")

sys.path.append(PROJECT_DIR)

import inputProcessors.formatDocstrings

def Main():
    """
    Discover all the tests in the tests directory adjacent this file and run them
    """
    parser = argparse.ArgumentParser(prog="AoC Maker", description="Create the test, solver, and input files for a given day")
    parser.add_argument("-d", "--day")

    args = parser.parse_args()

    if args.day:
        day = int(args.day)

        with open(SOLVER_TEMPLATE_FILE, 'r') as fh:
            daySolver = fh.read()

            daySolver = daySolver.replace('"$DAY"', args.day)

            daySolverFilePath = os.path.join(PROJECT_DIR, 'solutions', f'day{str(day).zfill(2)}.py')

            with open(daySolverFilePath, 'w') as outFH:
                outFH.write(daySolver)

            inputProcessors.formatDocstrings.formatDocstring(daySolverFilePath)

        with open(TEST_TEMPLATE_FILE, 'r') as fh:
            testContent = fh.read()

            testContent = testContent.replace('$DAY', str(day).zfill(2))

            testFilePath = os.path.join(PROJECT_DIR, 'tests', f'test_day{str(day).zfill(2)}.py')

            with open(testFilePath, 'w') as outFH:
                outFH.write(testContent)

        inputFilePath = os.path.join(INPUT_DIR, f'day{str(day).zfill(2)}.txt')

        with open(inputFilePath, 'w') as fh:
            fh.write("")


if __name__ == '__main__':
    Main()
