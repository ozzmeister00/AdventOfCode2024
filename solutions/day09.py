"""
"""

import itertools

import solver.runner
import solver.solver


class File(object):
    def __init__(self, blockId: int, size: int, freeSpace: int) -> None:
        self.id = blockId
        self.size = size
        self.freeSpace = freeSpace


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__(9, rawData=rawData)

    def ProcessInput(self) -> list[File]:
        """
        :returns list[File]
        """
        mapped = list(map(int, self.rawData))
        fileList = []
        index = 0
        for batch in list(itertools.batched(mapped, n=2)):
            blockSize = batch[0]
            freeSpace = batch[1] if len(batch) > 1 else 0
            fileList.append(File(index, blockSize, freeSpace))
            index += 1

        return fileList

    def SolvePartOne(self) -> int:
        """
        :return int: the checksum of the filesystem
        """
        # build out the full map of the harddrive
        harddrive = []
        for fileInfo in self.processed:
            harddrive.extend([fileInfo.id] * fileInfo.size)
            harddrive.extend([-1] * fileInfo.freeSpace)

        # defrag the drive by moving the right-most occupied block to the left-most available free space
        # until all free space is on the right
        numFree = harddrive.count(-1)
        for i in range(numFree):
            firstFree = harddrive.index(-1)
            harddrive.pop(firstFree)
            # pop the end of the array off and put it where we found a free space
            harddrive.insert(firstFree, harddrive.pop())

        result = 0
        for index, blockID in enumerate(harddrive):
            result += (index * blockID)

        return result

    def SolvePartTwo(self) -> int:
        """
        :return int: the checksum of the partially defragged filesystem
        """
        # make a copy of the harddrive in case something goes wrong
        fileSystem = self.processed.copy()

        # in decreasing fileID number, attempt to move the whole file to the leftmost available free space
        # if there is not a free space available, leave the file in place!

        searchOrder = fileSystem[::-1]

        # TODO don't try and do this in place, just build a new one?

        for fileInfo in searchOrder:
            for i, searchFileInfo in enumerate(fileSystem[:fileSystem.index(fileInfo)]):
                if searchFileInfo.freeSpace <= fileInfo.freeSpace:
                    fileSystem.pop(i)



        # then expand out the harddrive so we can generate the checksum
        harddrive = []
        for fileInfo in self.processed:
            harddrive.extend([fileInfo.id] * fileInfo.size)
            harddrive.extend([-1] * fileInfo.freeSpace)

        result = 0
        for index, blockID in enumerate(harddrive):
            result += (index * blockID)

        return result


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
