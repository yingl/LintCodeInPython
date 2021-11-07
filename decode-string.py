class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        if not s:
            return ''
        ret = []
        n = 0
        for c in s:
            if (c >= '0') and (c <= '9'):
                n = n * 10 + int(c)
            elif c == '[':
                ret.append(n)
                n = 0
            elif c == ']':
              _s = ''
              v = ret.pop()
              while type(v) != int:
                _s = v + _s
                v = ret.pop()
              ret.append(_s * v)
            else:
              ret.append(c)
        return ''.join(ret)
      
# medium: https://www.lintcode.com/problem/575
