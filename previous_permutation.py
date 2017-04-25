# coding: utf-8

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, num):
        # write your code here
        '''
        以162543为例，上一个应该是163534。
        步骤如下：
        1. 找到最后一个num[i] >= num[i - 1]的点
        2. 如果i = 0，逆序返回即可。
        3. 从num[i + 1]到num[-1]找到小于于num[i - 1]的最大数，并与num[i - 1]交换位置。
        4. 对num[i + 1]到num[-1]逆序排序
        '''
        i = len(num) - 1
        while i >= 1:
            if num[i] >= num[i - 1]:
                i -= 1
            else:
                break
        if i == 0:
            num.reverse()
            return num
        max_val, max_pos = num[i], i
        for j in xrange(i, len(num)):
            if (num[j] < num[i - 1]) and (num[j] > max_val):
                max_val = num[j]
                max_pos = j
        num[i - 1], num[max_pos] = num[max_pos], num[i - 1]
        partial_list = num[i:]
        partial_list.sort()
        partial_list.reverse()
        num[i:] = partial_list
        return num

# medium: http://lintcode.com/zh-cn/problem/previous-permutation/
