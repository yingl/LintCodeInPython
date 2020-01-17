class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        ret = 0 # There are no duplicated elements in each array
        di = {}
        for arr in arrs:
            for i in arr:
                if i in di:
                    di[i] += 1
                else:
                    di[i] = 1
        for k, v in di.items():
            if v == len(arrs):
                ret += 1
        return ret

# medium: https://www.lintcode.com/problem/intersection-of-arrays/
