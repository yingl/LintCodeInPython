class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        # Write your code here
        ret = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                ret += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r -= 1
        return ret
      
# easy: https://www.lintcode.com/problem/1784/
