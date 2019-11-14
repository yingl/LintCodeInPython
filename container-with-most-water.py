# coding: utf-8

class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        ret = 0
        begin, end = 0, len(heights) - 1
        while begin < end:
            vol = min(heights[begin], heights[end]) * (end - begin)
            if vol > ret:
                ret = vol
            if heights[begin] > heights[end]:
                # 右边向左移动直到heights[pos] > height[end]，只有这样，下一次结果才有可能比当前更大。
                pos = end - 1
                while (pos >= begin) and (heights[pos] <= heights[end]):
                    pos -= 1
                end = pos
            else:
                # 左边向右移动直到heights[pos] > height[begin]
                pos = begin + 1
                while (pos <= end) and (heights[pos] <= heights[begin]):
                    pos += 1
                begin = pos
        return ret

# medium: http://lintcode.com/zh-cn/problem/container-with-most-water/
