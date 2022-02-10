class Solution:
    """
    @param start: a point [x, y]
    @param target: a point [x, y]
    @return: return True or False
    """
    def ReachingPoints(self, start, target):
        # write your code here
        while start != target:
            if (target[0] < start[0]) or (target[1] < start[1]):
                return False
            if target[0] < target[1]:
                target[1] -= target[0]
            else:
                target[0] -= target[1]
        return True
