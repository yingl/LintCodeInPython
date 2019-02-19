class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    @staticmethod
    def check_same(left, right): # 反转180度依然保持一致的数字对
        return [left, right] in [['6', '9'], ['9', '6'], ['0', '0'], ['1', '1'], ['8', '8']]
        
    def isStrobogrammatic(self, num):
        # write your code here
        i, j = 0, len(num) - 1
        while i < j:
            if Solution.check_same(num[i], num[j]):
                i += 1
                j -= 1
            else:
                return False
        if i == j: # 反转180度依然保持一致的单个数字
            return num[i] in ['0', '1', '8']
        else:
            return True

# easy: https://www.lintcode.com/problem/strobogrammatic-number
