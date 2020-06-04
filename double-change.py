class Solution:
    def __init__(self):
        self.cache = {}

    """
    @param A: an Integer
    @param B: an Integer
    @param p: an Integer
    @param q: an Integer
    @return: Return the minimum time
    """
    def DoubleChange(self, A, B, p, q):
        # write your code here
        # 递归可以解决问，但是会超时。
        if A >= B:
            return 0
        if q == 1:
            return B - A
        else:
            cnt = 1
            diff = B - A
            while p < diff:
                p *= q
                cnt += 1
            return cnt
            
# easy: https://www.lintcode.com/problem/double-change/
