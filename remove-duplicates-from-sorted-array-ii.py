# coding: utf-8

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        num_dict = {}
        for i in xrange(0, len(A)):
            number = A[i]
            if number not in num_dict:
                num_dict[number] = 1
            else:
                num_dict[number] += 1
        for key, value in num_dict.items():
            if value < 2:
                del(num_dict[key])
            else:
                num_dict[key] = 0
        step = 0
        for i in xrange(0, len(A)):
            number = A[i]
            A[i - step] = number
            if number in num_dict:
                if num_dict[number] < 2:
                    num_dict[number] += 1
                else:
                    step += 1
        return len(A) - step

# easy: http://lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-array-ii/
