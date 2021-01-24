class Solution:
    """
    @param string: A string
    @return: whether the string is a valid parentheses
    """
    def matchParentheses(self, string):
        # write your code here
        s = []
        for c in string:
            if c == '(':
                s.append(c)
            else:
                if s and (s[-1] == '('):
                    s.pop()
                else:
                    return False
        return not s
        
# easy: https://www.lintcode.com/problem/matching-of-parentheses/
