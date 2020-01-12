class Solution:
    """
    @param S: string S
    @param T: string T
    @return: Backspace String Compare
    """
    def backspaceCompare(self, S, T):
        # Write your code here
        s = self.cleanBS(S)
        t = self.cleanBS(T)
        return s == t
        
    def cleanBS(self, s):
        ret = []
        for c in s:
            if c != '#':
                ret.append(c)
            elif ret:
                ret.pop()
        return ret
        
# easy: https://www.lintcode.com/problem/backspace-string-compare/
