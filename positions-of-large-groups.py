class Solution:
    """
    @param S: a string
    @return: the starting and ending positions of every large group
    """
    def largeGroupPositions(self, S):
        # Write your code here
        ret = []
        prev = S[0]
        count = [[0, 0]]
        for i in range(1, len(S)):
            c = S[i]
            if c == prev:
                count[-1][1] = i
            else:
                prev = c
                count.append([i, i])
        for c in count:
            if (c[1] - c[0]) >= 2:
                ret.append(c)
        return ret
        
# easy: https://www.lintcode.com/problem/positions-of-large-groups/
