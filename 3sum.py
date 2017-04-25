# coding: utf-8

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        self.ret = []
        numbers.sort()  # 排序后搜索，重点是去重！
        for i in xrange(len(numbers)):
            if i > 0:   # 第一个元素已经用过必需跳过
                if numbers[i] == numbers[i - 1]:
                    continue
            self.twoSum(numbers, -numbers[i], i + 1, len(numbers) - 1)
        return self.ret
        
    def twoSum(self, numbers, target, start, end):
        while start < end:
            x, y = numbers[start], numbers[end]
            if (x + y) == target:
                self.ret.append([-target, x, y])
                start += 1
                end -= 1
                # 跳过重复元素
                while (start < end) and (numbers[start] == x):
                    start += 1
                while (start < end) and (numbers[end] == y):
                    end -= 1
            elif (x + y) < target:
                start += 1
            else:
                end -= 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/3sum/
