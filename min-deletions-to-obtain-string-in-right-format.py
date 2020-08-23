class Solution:
    """
    @param s: the string
    @return: Min Deletions To Obtain String in Right Format
    """
    def minDeletionsToObtainStringInRightFormat(self, s):
        # write your code here
        ret = len(s)
        counting = []
        nums_a = 0
        nums_b = 0
        for c in s:
            counting.append([nums_b, 0])
            if c == 'B':
                nums_b += 1
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            counting[i][1] = nums_a
            if c == 'A':
                nums_a += 1
        for c in counting:
            s = c[0] + c[1]
            if s < ret:
                ret = s
        return ret
        
# easy: https://www.lintcode.com/problem/min-deletions-to-obtain-string-in-right-format/
