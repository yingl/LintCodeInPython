class Solution:
    """
    @param nums: the array
    @return: the third maximum number in this array
    """
    def thirdMax(self, nums):
        # Write your code here.
        ret = set([])
        for n in nums:
            if n not in ret:
                if len(ret) < 3:
                    ret.add(n)
                else:
                    m = min(ret)
                    if (m < n):
                        ret.remove(m)
                        ret.add(n)
        return max(ret) if len(ret) < 3 else min(ret)

# easy: https://www.lintcode.com/problem/third-maximum-number/description
