class Solution:
    """
    @param nums: 
    @param sub: 
    @return: return a Integer array
    """
    def SimpleQueries (self, nums, sub):
        # write your code here
        if not sub:
            return []
        ret, _ret = [0] * len(sub), [0]
        di = {}
        for i in range(len(sub)):
            if sub[i] not in di:
                di[sub[i]] = [i]
            di[sub[i]].append(i)
        nums.sort()
        sub.sort()
        i, j = 0, 0
        while i < len(nums):
            if nums[i] <= sub[j]:
                _ret[-1] += 1
                i += 1
            else:
                j += 1
                if j >= len(sub):
                    break
                _ret.append(_ret[-1])
        for k in range(j, len(sub)):
            _ret.append(_ret[-1])
        for k in range(len(sub)):
            ret[di[sub[k]][-1]] = _ret[k]
            di[sub[k]].pop()
        return ret

# medium: https://www.lintcode.com/problem/1791/
