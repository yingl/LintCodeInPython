class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        # Write your code here
        if (not s) or (not t):
            return False
        prev = -1
        ls, lt = 0, 0
        while (ls < len(s)) and (lt < len(t)):
            if s[ls] == t[lt]:
                ls += 1
                lt += 1
            else:
                ls += 1
        return lt == len(t)
      
# easy: https://www.lintcode.com/problem/1540/
