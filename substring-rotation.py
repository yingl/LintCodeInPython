class Solution:
    """
    @param s1: the first string
    @param s2: the second string
    @return: true if s2 is a rotation of s1 or false
    """
    def isRotation(self, s1, s2):
        # write your code here
        if (len(s1) != len(s2)) or (not (s1 and s2)):
            return False
        return Substring.isSubstring(s1 + s1, s2)
      
# easy: https://www.lintcode.com/problem/216/
