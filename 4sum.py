# coding: utf-8

class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        # write your code here
        self.ret = []
        self.numbers = numbers
        self.target = target
        self.numbers.sort() # 排序为了方便后面去重
        self.kSum(0, [], 0, 4)
        return self.ret

    def kSum(self, start, data, _sum, k):
        if k == 0:
            if _sum == self.target:
                self.ret.append(data[:])
        elif start < len(self.numbers):
            data.append(self.numbers[start])
            self.kSum(start + 1, data, _sum + self.numbers[start], k - 1)
            data.pop()
            j = start + 1 # 去重不要忘记
            while (j < len(self.numbers)) and (self.numbers[j] == self.numbers[start]):
                j += 1
            self.kSum(j, data, _sum, k)

# medium: http://lintcode.com/zh-cn/problem/4sum/
