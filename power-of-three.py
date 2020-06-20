class Solution:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        # Write your code here
        # 用log的方法我不认为合理，只是隐藏了循环。
        ret = False
        i = 1
        while i <= n:
            if i == n:
                ret = True
                break
            else:
                i *= 3
        return ret
        
# easy: https://www.lintcode.com/problem/power-of-three/
