from typing import (
    List,
)

class Solution:
    """
    @param arr: the array
    @return: determine the number of moves to make all elements equals
    """
    def array_game(self, arr: List[int]) -> int:
        # write your code here
        '''
        其它元素加1可以等价为该元素减1，其它元素不动。那么方法如下：
        1. 找到最小的元素
        2. 计算每个元素和这个最小元素的差
        3. 差加起来就是总步数
        '''
        r = 0
        m = min(arr)
        for i in arr:
            r += (i - m)
        return r
# medium: https://www.lintcode.com/problem/1907
