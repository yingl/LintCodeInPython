class Solution:
    """
    @param S: the string
    @return: The numbers of strings
    """
    def stretchWord(self, S):
        # write your code here
        ret = 0
        pc = None
        cnt = 0
        for c in S:
            if c != pc:
                pc = c
                cnt = 0
                if not ret:
                    ret = 1
            else:
                if cnt >= 1:
                    continue
                cnt += 1
                ret *= 2
        return ret
        
# easy: https://www.lintcode.com/problem/stretch-word/
