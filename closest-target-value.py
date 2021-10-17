class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        # Write your code here
        ret = None
        diff = 100000000 # max
        i, j = 0, len(array) - 1
        array.sort()
        while i < j:
            r = array[i] + array[j]
            if r == target:
                return r
            elif r > target:
                j -= 1
            else:
                if (target - r) < diff:
                    diff = target - r
                    ret = r
                i += 1
        return ret if ret else -1

# easy: https://www.lintcode.com/problem/1478/
