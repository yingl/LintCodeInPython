from typing import (
    List,
)

class Solution:
    """
    @param father: the father of every node
    @param time: the time from father[i] to node i
    @return: time to flower tree
    """
    def time_to_flower_tree(self, father: List[int], time: List[int]) -> int:
        # write your code here
        n = len(father)
        ret = [-1] * n
        ret[0] = 0
        for i in range(1, n):
            self.get_time(i, father, time, ret)
        return max(ret)

    def get_time(self, n, father, time, ret):
        f = father[n]
        if ret[f] == -1:
            ret[n] = time[n] + self.get_time(f, father, time, ret)
        else:
            ret[n] = time[n] + ret[f]
        return ret[n]
      
# medium: https://www.lintcode.com/problem/1862
