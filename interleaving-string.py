# coding: utf-8

class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        return self._isInterleave(s3, 0, s1, 0, s2, 0)
        
    def _isInterleave(self, s3, s3_start, s1, s1_start, s2, s2_start):
        if (s3_start == len(s3)) and (s1_start == len(s1)) and (s2_start == len(s2)):
            return True
        if (s1_start < len(s1)) and (s3[s3_start] == s1[s1_start]):
            if self._isInterleave(s3, s3_start + 1, s1, s1_start + 1, s2, s2_start):
                return True
        if (s2_start < len(s2)) and (s3[s3_start] == s2[s2_start]):
            if self._isInterleave(s3, s3_start + 1, s1, s1_start, s2, s2_start + 1):
                return True
        return False

# medium: http://lintcode.com/zh-cn/problem/interleaving-string/
