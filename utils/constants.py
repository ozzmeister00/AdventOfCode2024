"""
Constants and constant generators
"""

import os

UTILS_FOLDER = os.path.dirname(os.path.abspath(__file__))
SOURCE_FOLDER = os.path.split(UTILS_FOLDER)[0]

INPUTS_FOLDER_NAME = "inputData"
OUTPUTS_FOLDER_NAME = "outputData"


def getInputsFolder() -> str:
    """
    :return str: the absolute path on the file system to the inputData folder, which should be relative to this package
    """
    return os.path.join(SOURCE_FOLDER, INPUTS_FOLDER_NAME)


def getOutputsFolder() -> str:
    """
    :return str: the absolute path on the file system to the outputData folder
    """
    return os.path.join(SOURCE_FOLDER, OUTPUTS_FOLDER_NAME)


DIGITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
