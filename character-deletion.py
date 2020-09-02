class Solution:
    """
    @param str: The first string given
    @param sub: The given second string
    @return: Returns the deleted string
    """
    def CharacterDeletion(self, str, sub):
        # write your code here
        ret = []
        s = set(sub)
        for c in str:
            if c not in s:
                ret.append(c)
        return ''.join(ret)

# easy: https://www.lintcode.com/problem/character-deletion/
