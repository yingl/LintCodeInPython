class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def findTheDifference(self, s, t):
        # Write your code here
        di = {}
        for c in t:
            if c not in di:
                di[c] = 1
            else:
                di[c] += 1
        for c in s:
            di[c] -= 1
        for k, v in di.items():
            if v != 0:
                return k
                
# easy: https://www.lintcode.com/problem/find-the-difference/
