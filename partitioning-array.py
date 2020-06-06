class Solution:
    """
    @param A: Integer array
    @param k: a integer
    @return: return is possible to partition the array satisfying the above conditions
    """
    def PartitioningArray(self, A, k):
        # write your code here
        if len(A) % k != 0:
            return False
        di = {}
        for i in A:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1
            if di[i] > k:
                return False
        return True

# easy： https://www.lintcode.com/problem/partitioning-array/
