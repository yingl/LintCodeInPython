class Solution:
    """
    @param array: the input array
    @param k: the sequence length
    @return: if it is possible, return true, otherwise false
    """
    def partitionArratIII(self, array, k):
        # write your code here
        if (len(array) % k) != 0:
            return False
        n = len(array) / k
        di = {}
        for i in array:
            if i not in di:
                di[i] = 0
            di[i] += 1
        for k, v in di.items():
            if v > n:
                return False
        return True
        
# easy: https://www.lintcode.com/problem/partition-array-iii/
