class Solution:
    """
    @param s: A string with lowercase letters and parentheses
    @return: A string which has been removed invalid parentheses
    """
    def removeParentheses(self, s: str) -> str:
        # write your code here.
        r = []
        lps, rps = 0, 0
        for c in s:
            if c != ')':
                r.append(c)
                if c == '(':
                    lps += 1
            else:
              if rps < lps:
                r.append(c)
                rps += 1
        diff = lps - rps
        for i in range(len(r) - 1, -1, -1):
            if (r[i] == '(') and (diff > 0):
                r[i] = ''
                diff -= 1
                if diff == 0:
                  break
        return ''.join(r)
        
# easy: https://www.lintcode.com/problem/2506/
