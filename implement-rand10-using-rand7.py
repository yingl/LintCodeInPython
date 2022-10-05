class Solution(SolBase):
    def rand10(self):
        # 推导过程可以参考 https://www.jianshu.com/p/1127e746da12
        while True:
            i = (self.rand7() - 1) * 7 + (self.rand7() - 1)
            if (i >= 1) and (i <= 10): # 因为i在1-10之间均匀分布，超出的值不要！
                return i
              
# medium: https://www.lintcode.com/problem/1496
