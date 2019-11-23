# coding: utf-8

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i in xrange(numbers - 1):
            for j in xrange(i + 1, numbers):
                if (numbers[i] + numbers[j]) == target:
                    return [i + 1, j + 1]
        return [0, 0]

# easy: http://lintcode.com/zh-cn/problem/two-sum/
