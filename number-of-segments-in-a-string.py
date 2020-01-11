class Solution:
    """
    @param s: a string
    @return: the number of segments in a string
    """
    def countSegments(self, s):
        # write yout code here
        ret = 0
        is_word = False
        for c in s:
            if c != ' ':
                if not is_word:
                    ret += 1
                    is_word = True
            else:
                is_word = False
        return ret
        
# easy: https://www.lintcode.com/problem/number-of-segments-in-a-string/
