class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findShortestSubArray(self, nums):
        # write your code here
        di = {}
        for i in range(len(nums)):
            if nums[i] not in di:
                di[nums[i]] = [1, i, i]
            else:
                di[nums[i]][0] += 1
                di[nums[i]][2] = i
        candidates = []
        for k, v in di.items():
            if not candidates:
                candidates.append((k, v))
            else:
                if v[0] > candidates[-1][1][0]:
                    candidates = [(k, v)]
                elif v[0] == candidates[-1][1][0]:
                    candidates.append((k, v))
        # 以上把与度有关的元素找出来，同时记录度的值与起止位置。
        ret = len(nums)
        for c in candidates:
            l = c[1][2] - c[1][1] + 1
            if l < ret:
                ret = l
        return ret
        
# easy: https://www.lintcode.com/problem/degree-of-an-array/
