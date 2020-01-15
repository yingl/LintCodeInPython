from functools import cmp_to_key

class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        import functools
        return sorted(array, key=functools.cmp_to_key(self.my_cmp))

    @staticmethod        
    def my_cmp(x, y):
        if x[1] < y[1]:
            return 1
        else:
            if x[1] == y[1]:
                return -1 if x[0] < y[0] else 1
            return -1

# easy: https://www.lintcode.com/problem/multi-keyword-sort/
