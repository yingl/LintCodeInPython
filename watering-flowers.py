from typing import (
    List,
)

class Solution:
    """
    @param plants: 
    @param capacity1: 
    @param capacity2: 
    @return: 
    """
    def water_plants(self, plants: List[int], capacity1: int, capacity2: int) -> int:
        # 
        ret = 0
        n = len(plants)
        c1, c2 = 0, 0
        n1, n2 = 0, n - 1
        while n1 < n2:
            if c1 < plants[n1]:
                c1 = capacity1
                ret += 1
            if c2 < plants[n2]:
                c2 = capacity2
                ret += 1
            c1 -= plants[n1]
            c2 -= plants[n2]
            n1 += 1
            n2 -= 1
        if (n1 == n2) and (plants[n1] > (c1 + c2)):
            return ret + 1
        else:
            return ret
            
# medium: https://www.lintcode.com/problem/1518
