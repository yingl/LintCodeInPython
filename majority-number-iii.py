# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        # 还是借鉴majority_number_ii.py的算法
        statistics = {}
        for num in nums:
            if num in statistics:
                statistics[num] += 1
            elif len(statistics) < k:
                statistics[num] = 1
            else:
                keys = []
                for key in statistics:
                    statistics[key] -= 1
                    if statistics[key] == 0:
                        keys.append(key)
                for key in keys:
                    del(statistics[key])
        ret, _max_count = None, 0
        for num in nums:
            if num in statistics:
                statistics[num] += 1
                if statistics[num] > _max_count:
                    _max_count = statistics[num]
                    ret = num
        return ret

# medium: http://lintcode.com/zh-cn/problem/majority-number-iii/
