class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """
    def canConstruct(self, ransomNote, magazine):
        # Write your code here
        di = {}
        for c in magazine:
            if c not in di:
                di[c] = 1
            else:
                di[c] += 1
        for c in ransomNote:
            if c not in di:
                return False
            else:
                di[c] -= 1
                if di[c] < 0:
                    return False
        return True

# easy: https://www.lintcode.com/problem/ransom-note/
