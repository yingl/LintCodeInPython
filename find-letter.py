class Solution:
    """
    @param str: the str
    @return: the letter
    """
    def findLetter(self, _str):
        # Write your code here.
        di = {}
        for c in _str:
            u_c = c.upper()
            if u_c not in di:
                di[u_c] = 0
            if c == u_c:
                di[u_c] |= 2
            else:
                di[u_c] |= 1
        ret = None
        for k, v in di.items():
            if v == 3:
                if not ret:
                    ret = k
                else:
                    if k > ret:
                        ret = k
        return ret if ret else '~'

# easy: https://www.lintcode.com/problem/find-letter/
