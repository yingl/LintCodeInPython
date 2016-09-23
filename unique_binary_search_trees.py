class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        # write your code here
        # 只需要计算数量，不需要计算每棵树的形状，所以缓存结果就可以了。
        if n == 0:
            return 1
        methods = [0] * (n + 1)
        methods[0], methods[1] = 1, 1
        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                methods[i] += methods[j - 1] * methods[i - j]
        return methods[-1]