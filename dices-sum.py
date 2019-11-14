# coding: utf-8

class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        '''
        只有1个骰子，概率是1/6。
        对于有2个骰子的情况，以第一个骰子为基础算，m[x][y]代表x个骰子获得y点。
        m[2][7]等于以下状态的和：
        - m[1][1] / 6（出6点）
        - m[1][2] / 6（出5点）
        - m[1][3] / 6（出4点）
        - m[1][4] / 6（出3点）
        - m[1][5] / 6（出2点）
        - m[1][6] / 6（出1点）
        '''
        ret = []
        matrix = [[0] * (n * 6) for i in xrange(n)]
        for i in xrange(6): # 初始化1个骰子的结果
            matrix[0][i] = 1.0 / 6.0
        for i in xrange(n - 1):
            for j in xrange(i, (i + 1) * 6):
                prob = matrix[i][j] / 6
                for k in xrange(1, 7):
                  # 利用matrx[i][j]更新matrix[i + 1][j + k]
                  matrix[i + 1][j + k] += prob
        for i in xrange(n - 1, n * 6):
            ret.append([i + 1, matrix[-1][i]])
        return ret

# hard: http://lintcode.com/problem/dices-sum
