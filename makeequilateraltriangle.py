class Solution:
    """
    @param lengths: the lengths of sticks at the beginning.
    @return: return the minimum number of cuts.
    """
    def makeEquilateralTriangle(self, lengths):
        # write your code here.
        ret = 2
        s = set(lengths)
        lengths.sort()
        for i in range(len(lengths) - 2):
            i1 = lengths[i]
            i2 = lengths[i + 1]
            i3 = lengths[i + 2]
            if (i1 == i2) and (i2 == i3):
                return 0
            elif (i1 == i2) or (i2 == i3) or ((i1 * 2) in s):
                ret = 1
        return ret
        
# easy: https://www.lintcode.com/problem/makeequilateraltriangle/
