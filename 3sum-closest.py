# coding: utf-8

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        ret = -1
        min_diff = 2147483647
        numbers.sort()  # 先排序，排序后两个指针从头尾向中间找。
        for i in xrange(len(numbers) - 2):
            start, end = i + 1, len(numbers) - 1
            while start < end:
                three_sum = numbers[i] + numbers[start] + numbers[end]
                diff = abs(three_sum - target)
                if diff == 0:
                    return target
                if diff < min_diff:
                    min_diff = diff
                    ret = three_sum
                if three_sum < target:
                    start += 1
                else:
                    end -= 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/3sum-closest/
