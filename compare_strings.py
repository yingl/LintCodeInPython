# coding: utf-8

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if not B:
            return True
        count  = {}
        for i, ch in enumerate(B):
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
        for i, ch in enumerate(A):
            if ch in count:
                count[ch] -= 1
                if count[ch] == 0:
                    del(count[ch])
        return not count

# easy: http://lintcode.com/zh-cn/problem/compare-strings/
