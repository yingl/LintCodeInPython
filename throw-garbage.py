class Solution:
    """
    @param BagList: the weight of all garbage bags.
    @return: an integer represent the minimum number of times.
    """
    def Count_ThrowTimes(self, BagList):
        #
        # Because at least the bag is 1.01, so you can take at most 2 bags at 1 time!
        r = 0
        BagList.sort()
        i, j = 0, len(BagList) - 1
        while i < j:
            s = BagList[i] + BagList[j]
            if s > 3:
                j -= 1
            else:
                i += 1
                j -= 1
            r += 1
        if i == j:
            r += 1
        return r
