class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here
        # 不排序的话得参考鸽笼原理。
        # 如果有n个数，那么根据平均距离把数据分段，
        # 那么最大值一定是某个区间的最小值减去上个区间的最大值（一定相邻）。
        # 为什么不在一个区间内呢？鸽笼原理的限制。
        # 下面有一些技巧性的处理：因为要分区间，所以即使有2个数也要拆到2个区间。
        # 以下数据举例：[1, 3, 4, 8, 10, 12]，进行以下处理：
        # - 平均间隔：(12 - 1) / (6 - 1) = 2.2，向下取整为2。
        # - 那么可以用这个公式：int((12 - 1) / 6) + 1 = 2
        # 如果是递增数列[1, 3, 5, 7, 9]那么上面两个公式是等价的：
        # - (9 - 1) / (5 - 1) = 2
        # - int((9 - 1) / 5) + 1 = 2
        # 根据期望长度（实际平均长度不小于这个值），我们可以对数据进行分段。
        ret = 0
        if len(nums) >= 2:
            _min, _max = min(nums), max(nums)
            size = int((_max - _min) / len(nums)) + 1 # 这两个处理比较有技巧性
            buckets = int((_max - _min) / size) + 1
            min_bucket = [_max + 1] * buckets
            max_bucket = [_min - 1] * buckets
            for i in nums:
                idx = int((i - _min) / size)
                min_bucket[idx] = min(i, min_bucket[idx])
                max_bucket[idx] = max(i, max_bucket[idx])
            idx = 0
            while idx < buckets:
                while max_bucket[idx] == (_min - 1): # 不用担心越界
                    idx += 1
                idx_2 = idx + 1
                if idx_2 >= buckets:
                    break
                while min_bucket[idx_2] == (_max + 1):
                    idx_2 += 1
                ret = max(ret, min_bucket[idx_2] - max_bucket[idx])
                idx = idx_2
        return ret

# medium: https://www.lintcode.com/problem/maximum-gap/
