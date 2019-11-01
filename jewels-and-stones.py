class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        ret = 0
        s = set(J)
        for c in S:
            if c in s:
                ret += 1
        return ret

# easy: https://www.lintcode.com/problem/jewels-and-stones/
