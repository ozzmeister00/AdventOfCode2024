from itertools import tee, islice
from typing import Iterator, Iterable, TypeVar


T = TypeVar('T')
def window(iterable: Iterable[T], n: int) -> Iterator[tuple[T, ...]]:
    """
    Creates a sliding window of size n as an iterator

    :param iterable the input iterator:
    :param n size of the window:
    :return Iterator[tuple[T, ...]:
    """
    slices = (islice(it, i, None) for i, it in enumerate(tee(iterable, n)))
    return zip(*slices)


def headsAndTails(index: int, inList: list) -> tuple[list, list]:
    """
    Split the input list into two, omitting the input index and returning
    slices on either side of that index

    :param index:
    :param inList:
    :return:
    """
    # special case handling for the last index
    if index == len(inList)-1:
        return inList[:-1], []

    return inList[:index], inList[index:]


class defaultlist(list):
    """
    A class that will automatically populate itself with values
    if accessing or setting indexes that are outside of its 
    current size
    """
    def __init__(self, cls, *args, **kwargs):
        """
        :param Class cls: the default class with which to instantiate new values
        """
        super(defaultlist, self).__init__(*args, **kwargs)
        self._cls = cls

    def _fill(self, index):
        while len(self) <= index:
            self.append(self._cls())

    def __getitem__(self, index):
        self._fill(index)
        return super(defaultlist, self).__getitem__(index)

    def __setitem__(self, index, value):
        self._fill(index)
        return super(defaultlist, self).__setitem__(index, value)


class DefaultIndexList(defaultlist):
    """
    Override the functionality of defaultlist to pass
    the index we're appending to the fill function
    """
    def __init__(self):
        super(DefaultIndexList, self).__init__(int)

    def _fill(self, index):
        while len(self) <= index:
            self.append(self._cls(index))
