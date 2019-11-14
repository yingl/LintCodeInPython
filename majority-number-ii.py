# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        '''
        基本思想就是出现3个不同的数就消掉，而主元素因为数量大于1/3所以必定会保存下来。
        具体实现如下：
        1. 通过v1、v2和c1、c2记录当前的2个数和出现次数。
        2. 如果第三个数都不匹配，c1和c2各减1，代表删除1个。
        3. 如果匹配其中一个，计数加1。
        4. 最后剩下的v1、v2比较，返回数量更多的那个。
        '''
        v_1, c_1 = None, 0
        v_2, c_2 = None, 0
        for num in nums:
            if num == v_1:
                c_1 += 1
            elif num == v_2:
                c_2 += 1
            elif c_1 == 0:
                v_1 = num
                c_1 = 1
            elif c_2 == 0:
                v_2 = num
                c_2 = 1
            else:
                c_1 -= 1
                c_2 -= 1
        c_1, c_2 = 0, 0
        for num in nums:
            if num == v_1:
                c_1 += 1
            elif num == v_2:
                c_2 += 1
        return v_1 if c_1 >= c_2 else v_2

# medium: http://lintcode.com/zh-cn/problem/majority-number-ii/
