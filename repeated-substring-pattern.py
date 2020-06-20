class Solution:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeatedSubstringPattern(self, s):
        # write your code here
        for i in range(1, int(len(s) / 2) + 1):
            if (len(s) % i) == 0:
                ns = s[:i] * int(len(s) / i)
                if ns == s:
                    return True
        return False
        
# easy: https://www.lintcode.com/problem/repeated-substring-pattern/
