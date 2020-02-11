class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """
    def numberOfBoomerangs(self, points):
        # Write your code here
        ret = 0
        for i in range(len(points)):
            di = {} # 根据距离记录点位对数
            total = 0
            for j in range(len(points)): # 元组的顺序是重要的！！！
                if i != j: # 每一对点都是不同的！！！
                    dist = pow(points[j][0] - points[i][0], 2) + \
                           pow(points[j][1] - points[i][1], 2)
                    if dist in di:
                        # 在已有di[dist]对点位的情况下，
                        # 每新增一个点位但表增加了di[dist]种[i, j, k]组合。
                        # [i, j, k]又可以变成[i, k, j]，所以后面要乘2.
                        total += di[dist]
                        di[dist] += 1
                    else:
                        di[dist] = 1 # 有一对点位
            print(i, total)
            ret += total * 2
        return ret

# easy: https://www.lintcode.com/problem/number-of-boomerangs/
