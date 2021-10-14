class Solution:
    """
    @param nums: a integer array
    @return: return an integer denoting the number of non-unique(duplicate) values
    """
    def countduplicates(self, nums):
        # write your code here
        r = []
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = [-1, 1]
            else:
                m[nums[i]][1] += 1
                if m[nums[i]][0] == -1:
                    m[nums[i]][0] = i
        for k, v in m.items():
            if v[1] == 1:
                m[k] = len(nums)
            else:
                m[k] = v[0]
        s = sorted(m.items(), key = lambda kv: (kv[1], kv[0]))
        for kv in s:
            if kv[1] < len(nums):
                r.append(kv[0])
        return r
      
# easy: https://www.lintcode.com/problem/1794/
