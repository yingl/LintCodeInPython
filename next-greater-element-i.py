class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        # 如何理解题目：
        #   - 对于nums1的数字i，先找到它在nums2的位置。
        #   - 然后从这个位置开始，找到第一个比它大的数。
        # 所以我们可以先构造一张表，对于nums2的每个元素i，记录后面出现的第一个比它大的数。
        # 重点关注for-while代码：
        #   - 如果堆栈为空，当前元素入栈。
        #   - 继续for循环，如果当前堆栈不为空，且大于堆栈最后一个元素！！！
        #     记住，堆栈内的元素顺序是与for循环同样顺序进入的。
        #     那么这个元素后第一个出现的比它大的元素找到，弹出并构造字典关系。
        #     继续循环，之前满足的也一起构造了。
        di = {}
        stack = []
        for i in nums2:
            while stack and (stack[-1] < i):
                di[stack.pop()] = i
            stack.append(i)
        return [di.get(i, -1) for i in nums1]

# easy: https://www.lintcode.com/problem/next-greater-element-i/
