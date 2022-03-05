from typing import (
    List,
)

class Solution:
    """
    @param a: An Integer array
    @return: returns the maximum sum of two numbers
    """
    def maximum_sum(self, a: List[int]) -> int:
        # write your code here
        r = -1
        di = {}
        for i in a:
            d = 0
            j = i
            while j > 0:
                d += j % 10
                j = int(j / 10)
            if d not in di:
                di[d] = []
            di[d].append(i)
        for k, v in di.items():
            if len(v) >= 2:
                v.sort()
                s = v[-1] + v[-2]
                if s > r:
                    r = s
        return r
      
# medium: https://www.lintcode.com/problem/1604/
