class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here
        di = {}
        for c in str:
            if c not in di:
                di[c] = 1
            else:
                di[c] += 1
        return di
      
# easy: https://www.lintcode.com/problem/557
