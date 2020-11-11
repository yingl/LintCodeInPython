class Solution:
    """
    @param s: a string
    @return: a string
    """
    def largestLetter(self, s):
        # write your code here
        ret = 'NO'
        cs = set([])
        for c in s:
            cs.add(c)
        for c in s:
            if (c.lower() in cs) and (c.upper() in cs):
                if ret == 'NO':
                    ret = c.upper()
                else:
                    if c.upper() > ret:
                        ret = c.upper()
        return ret
        
# easy: https://www.lintcode.com/problem/largest-letter/
