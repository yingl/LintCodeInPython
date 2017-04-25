# coding: utf-8

class Solution:
    # @param {int[]} ratings Children's ratings
    # @return {int} the minimum candies you must give
    def candy(self, ratings):
        # Write your code here
        '''
        题目的表达有问题，并不是等级越高糖越多。
        比如[1, 2, 2]的情况，
        因为当中的2比1大，所以分2块，而最右边的2只是和左边的2相等，所以只分1块。
        思路如下：
        1. 初始化每人至少1颗糖。
        2. 从左向右遍历，如果比前面等级高，那么比前面多分一粒糖。
        3. 从右往左遍历，如果比后面等级高，并且不比后面的糖多，那么比后面多分一粒糖。
        '''
        if not ratings:
            return 0
        candies = [1 for i in xrange(len(ratings))]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in xrange(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if candies[i] <= candies[i + 1]:
                    candies[i] = candies[i + 1] + 1
        return sum(candies)

# hard: http://lintcode.com/zh-cn/problem/candy/
