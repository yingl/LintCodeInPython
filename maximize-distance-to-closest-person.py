class Solution:
    """
    @param seats: an array
    @return: the maximum distance
    """
    def maxDistToClosest(self, seats):
        # Write your code here.
        ret = 0
        prev = -1
        mid, head, tail = -1, -1, -1
        for i in range(len(seats)):
            if seats[i] != 0:
                if prev != -1:
                    mid = max(mid, i - prev - 1)
                else:
                    head = i
                prev = i
        if prev != (len(seats) - 1):
            tail = len(seats) - prev - 1 # 因为至少1个1
        return max(int((mid + 1) / 2), head, tail)
        
# easy: https://www.lintcode.com/problem/maximize-distance-to-closest-person/
