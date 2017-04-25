# coding: utf-8

class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        ret = 0
        if heights:
            begin, end = 0, len(heights) - 1
            l_max, r_max = 0, 0
            while begin < end:
                l_max = max(l_max, heights[begin])
                r_max = max(r_max, heights[end])
                if l_max > r_max:
                    '''
                    因为左边更高，右边继续向左移动。
                    当前位置的容量为右边最大值减去高度。
                    '''
                    ret += r_max - heights[end]
                    end -= 1
                else:
                    ret += l_max - heights[begin]
                    begin += 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/trapping-rain-water/
