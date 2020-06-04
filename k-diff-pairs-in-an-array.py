class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        ret = 0
        if len(nums) >= 2:
            di = {}
            for i in nums:
                if i not in di:
                    di[i] = 1
                else:
                    di[i] += 1
            k = abs(k)
            used = set([])
            for i in nums:
                if k == 0:
                    if (i not in used) and (di[i] > 1):
                        ret += 1
                        used.add(i)
                else:
                    if i not in used:
                        if (i + k) in di:
                            ret += 1
                            used.add(i)
        return ret

# easy: https://www.lintcode.com/problem/k-diff-pairs-in-an-array/
