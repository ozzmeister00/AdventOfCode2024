from unittest import TestCase

import utils.list


class Test(TestCase):
    def test_defaultlist(self):
        l = utils.list.defaultlist(int)
        
        # make sure the array will size itself properly when getting a value
        # outside of its current size)
        self.assertEqual(0, l[5])

        # make sure the array can resize itself when setting a value
        l[8] = 8

        # and that we can retrieve that value
        self.assertEqual(8, l[8])

    def test_headsAndTails(self):
        l = [0, 1, 2, 3, 4, 5]
        expectedHead, expectedTail = [0, 1], [3, 4, 5]
        heads, tails = utils.list.headsAndTails(2, l)

        self.assertEqual(expectedHead, heads)
        self.assertEqual(expectedTail, tails)
