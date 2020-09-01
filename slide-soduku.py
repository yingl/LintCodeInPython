class Solution:
    """
    @param number: an only contains from 1 to 9 array
    @return: return  whether or not each sliding window position contains all the numbers for 1 to 9 
    """
    def SlidingWindows(self, number):
        # write your code here
        ret = []
        n = len(number[0])
        for start in range(0, n - 2):
            s = set([])
            for r in range(3):
                for c in range(3):
                    s.add(number[r][c + start])
            ret.append(len(s) == 9)
        return ret

# easy: https://www.lintcode.com/problem/slide-soduku/
