class Solution:
    """
    @param nums: an array
    @return: the minimum number of moves required to make all array elements equal
    """
    def minMoves(self, nums):
        # Write your code here
        # 为了快速的缩小差距，该选择哪些数字加1呢，不难看出每次需要给除了数组最大值的所有数字加1，
        # 这样能快速的到达平衡状态。但是每次都要找到最大值，复杂度不允许啊。
        # 
        # 其实给n-1个数字加1，效果等同于给那个未被选中的数字减1，比如数组[1，2，3], 
        # 给除去最大值的其他数字加1，变为[2，3，3]，我们全体减1，并不影响数字间相对差异，
        # 变为[1，2，2]，这个结果其实就是原始数组的最大值3自减1，
        # 那么问题也可能转化为，将所有数字都减小到最小值，这样难度就大大降低了，
        # 我们只要先找到最小值，然后累加每个数跟最小值之间的差值即可。
        ret = 0
        if len(nums) >= 2:
            _min = min(nums)
            for i in nums:
                ret += i - _min
        return ret

# easy: https://www.lintcode.com/problem/minimum-moves-to-equal-array-elements/
