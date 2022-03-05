from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        # write your code here
        r = len(nums) + 1
        s = 0
        di = {0: [-1]}
        for i in range(len(nums)):
            s += nums[i]
            if s not in di:
                di[s] = []
            di[s].append(i)
        for s, ids in di.items():
            t = s - k
            if t in di:
                for i in ids:
                    for j in di[t]:
                        if i > j:
                            r = min(r, i - j)
        return r if r <= len(nums) else -1
      
# medium: https://www.lintcode.com/problem/1844/
