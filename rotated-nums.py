class Solution:
    def __init__(self):
        self.cache = {1: 5, 2: 6, 3: 30}
        
    """
    @param n: length of good nums
    @return: The num of good nums of length n
    """
    def RotatedNums(self, n):
        # write your code here
        init = [0, 5, 6, 30]
        if n <= 3:
            return init[n]
        start = 2 if (n % 2) == 0 else 3
        steps = int((n - start) / 2) # 一定要取整数，不然浮点数计算精度会有问题。
        return int(init[start] * pow(7, steps))
        
# easy: https://www.lintcode.com/problem/rotated-nums/
