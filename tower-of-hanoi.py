class Solution:
    """
    @param n: the number of disks
    @return: the order of moves
    """
    def towerOfHanoi(self, n):
        # write your code here
        ret = []
        if n > 0:
            Solution.move(n, 'A', 'C', 'B', ret)
        return ret
        
    @staticmethod
    def move(n, source, target, by, ret):
        if n == 1:
            ret.append('from %s to %s' % (source, target))
        else:
            Solution.move(n - 1, source, by, target, ret)
            ret.append('from %s to %s' % (source, target))
            Solution.move(n - 1, by, target, source, ret)

# medium: http://lintcode.com/zh-cn/problem/tower-of-hanoi/
