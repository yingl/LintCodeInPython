class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here
        if not S:
            return ['']
        ret = []
        perms = self.letterCasePermutation(S[1:])
        for perm in perms:
            if self.is_digit(S[0]):
                ret.append(S[0] + perm)
            else:
                ret.append(S[0].lower() + perm)
                ret.append(S[0].upper() + perm)
        return ret

    def is_digit(self, c):
        return c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# easy: https://www.lintcode.com/problem/letter-case-permutation/
