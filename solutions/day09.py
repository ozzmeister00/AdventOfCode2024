"""
Upon completion, two things immediately become clear. First, the disk definitely has a lot 
more contiguous free space, just like the amphipod hoped. Second, the computer is running 
much more slowly! Maybe introducing all of that file system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like
 to try compacting the files on his disk by moving whole files instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could
 fit the file. Attempt to move each file exactly once in order of decreasing file ID number
  starting with the file with the highest file ID number. If there is no span of free space 
  to the left of a file that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method instead. 
What is the resulting filesystem checksum?


"""
import copy
import itertools
import sys

import utils.list

import solver.runner
import solver.solver

# version compatibility for itertools.batched
if sys.version_info.minor < 12:
    itertools.batched = utils.list.batched

class File(object):
    def __init__(self, blockId: int, size: int, freeSpace: int) -> None:
        self.id = blockId
        self.size = size
        self.freeSpace = freeSpace

    def __eq__(self, other) -> bool:
        if isinstance(other, File):
            return self.id == other.id and self.size == other.size
        else:
            raise ValueError(f"Cannot compare type {str(type(other))} with File")


class FileSystem(list):
    def __init__(self, rawData: str):
        super(FileSystem, self).__init__()

        mapped = list(map(int, rawData))
        index = 0
        for batch in list(itertools.batched(mapped, 2)):
            blockSize = batch[0]
            freeSpace = batch[1] if len(batch) > 1 else 0
            self.append(File(index, blockSize, freeSpace))
            index += 1

    def expandToBlocks(self) -> list[int]:
        """
        Return an expanded version of the harddrive as individual blocks
        where each item in the returned list is equal to the id of the 
        file that occupies that block. If the space is free, the value 
        is -1
        """
        harddrive = []
        for fileInfo in self:
            harddrive.extend([fileInfo.id] * fileInfo.size)
            harddrive.extend([-1] * fileInfo.freeSpace)

        return harddrive

    def checksum(self) -> int:
        """
        Generate the checksum of the harddrive by 
        multiplying the file ID by its position in the harddrive
        """
        harddrive = self.expandToBlocks()
        result = 0
        for index, blockID in enumerate(harddrive):
            if blockID > -1:
                result += (index * blockID)

        return result

    def __str__(self) -> str:
        harddrive = self.expandToBlocks()

        fileSystemStr = ''

        for i, value in enumerate(harddrive):
            fileSystemStr += '.' if value == -1 else str(value)

        return fileSystemStr


class Solver(solver.solver.ProblemSolver):
    def __init__(self, rawData=None):
        super(Solver, self).__init__(9, rawData=rawData)

    def ProcessInput(self) -> FileSystem:
        """
        :return: raw data translated into a FileSystem
        """
        return FileSystem(self.rawData)


    def SolvePartOne(self) -> int:
        """
        :return int: the checksum of the filesystem
        """
        # build out the full map of the harddrive
        harddrive = self.processed.expandToBlocks()

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
        fileSystem = copy.copy(self.processed)

        # in decreasing fileID number, attempt to move the whole file to the leftmost available free space
        # if there is not a free space available, leave the file in place!

        # search order is reversed of the file system
        searchOrder = fileSystem[::-1]

        # TODO don't try and do this in place, just build a new one?

        for fileInfo in searchOrder:
            searchIndex = 0
            currentFileInfoIndex = fileSystem.index(fileInfo)
            while searchIndex < currentFileInfoIndex:
                searchFileInfo = fileSystem[searchIndex]
                if searchFileInfo.freeSpace >= fileInfo.size:
                    
                    fileInfoIndex = fileSystem.index(fileInfo)

                    # move the free space and block size of the current fileInfo
                    # to the block preceeding its current spot in the file system
                    prevFileIndex = fileInfoIndex - 1
                    fileSystem[prevFileIndex].freeSpace += fileInfo.size + fileInfo.freeSpace
                    
                    # then move the free space to the end of the current block
                    fileInfo.freeSpace = searchFileInfo.freeSpace - fileInfo.size
                    # and set the free space of the test block to 0
                    searchFileInfo.freeSpace = 0

                    # pull the fileInfo out of the file system
                    fileSystem.pop(fileInfoIndex)

                    # so we can put it back after the current test block
                    fileSystem.insert(searchIndex + 1, fileInfo)

                    # and push the searchIndex beyond the limits to break out of the loop
                    searchIndex = len(fileSystem)

                searchIndex += 1

        return fileSystem.checksum()


if __name__ == '__main__':
    daySolver = Solver()
    if solver.runner.RunTests(daySolver.day):
        daySolver.Run()
