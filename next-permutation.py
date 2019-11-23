# coding: utf-8

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        # write your code here
        '''
        以162543为例，下一个应该是163245。
        步骤如下：
        1. 找到最后一个num[i] < num[i + 1]的点
        2. 如果没找到，说明已经是最后一个排列，逆序返回即可。
        3. 从num[i + 1]到num[-1]找到大于num[i]的最小数，并与num[i]交换位置。
        4. 对num[i + 1]到num[-1]排序
        '''
        i = len(num) - 2
        while i >= 0:
            if num[i] < num[i + 1]:
                break
            i -= 1
        if i < 0:
            num.reverse()
            return num
        min_val = num[i + 1]
        min_pos = i + 1
        for j in xrange(i + 2, len(num)):
            if (num[j] < min_val) and (num[j] > num[i]):
                min_val, min_pos = num[j], j
        num[i], num[min_pos] = num[min_pos], num[i]
        partial_list = num[i + 1:]
        partial_list.sort()
        num[i + 1:] = partial_list
        return num

# medium: http://lintcode.com/zh-cn/problem/next-permutation/
