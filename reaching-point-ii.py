class Solution:
    """
    @param start: a point [x, y]
    @param target: a point [x, y]
    @return: return True and False
    """
    def ReachingPointsII(self, start, target):
        # write your code here
        '''
        Look somebody's clue, it's really interesting!
        if target-y > target-x, it means it comes from (x, y) to (x, x + y)， vice versa.
        So you should immediately know what to do, but do minus is too slow!
        Think about [1, 1] to [1, 1,000,000,000]...
        Let's make a example: [4, 15], run this way:
          - [4, 11]
          - [4, 7]
          - [4, 3] 11 % 4 = 3, so let's go!!!
        '''
        while (start[0] < target[0]) and (start[1] < target[1]):
            if target[1] > target[0]:
                target[1] %= target[0]
            else:
                target[0] %= target[1]
        f1 = (start[0] == target[0]) and (((target[1] - start[1]) % start[0]) == 0)
        f2 = (start[1] == target[1]) and (((target[0] - start[0]) % start[1]) == 0)
        return f1 or f2

# medium: https://www.lintcode.com/problem/1846
