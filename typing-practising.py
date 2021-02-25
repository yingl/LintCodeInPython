class Solution:
    """
    @param s: A string
    @return: A string
    """
    def getTextcontent(self, s):
        # write your code here.
        chars = []
        for c in s:
            if c != '<':
                chars.append(c)
            else:
                if chars:
                    chars.pop()
        return ''.join(chars)
      
# easy: https://www.lintcode.com/problem/typing-practising/
