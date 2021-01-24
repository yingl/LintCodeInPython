class Solution:
    """
    @param operation: A list of operations.
    @return: The lamp has the longest liighting time.
    """
    def longestLightingTime(self, operation):
        # write your code here
        ret = 0
        lst = 0
        pt = 0
        for op in operation:
            t = op[1] - pt
            if t > lst:
                lst = t
                ret = op[0]
            pt = op[1]
        return chr(ord('a') + ret)
        
# easy: https://www.lintcode.com/problem/longest-lighting-time/
