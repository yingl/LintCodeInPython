class Solution:
    """
    @param array: An given array.
    @return: Return the number of "universal" subarrays.
    """
    def subarrays(self, array):
        # write your code here.
        '''
        只能出现[x, x, x, y, y, y]的形式
        思路：记录每个字符连续出多少次。
        - 如果x出现a次，y出现b次。
        - 可以生成min(a, b)个子序列。
        '''
        ret = 0
        prev = array[0]
        count = [1]
        for i in range(1, len(array)):
            c = array[i]
            if c == prev:
                count[-1] += 1
            else:
                prev = c
                count.append(1)
        for i in range(1, len(count)):
            ret += min(count[i - 1], count[i])
        return ret
        
# easy: https://www.lintcode.com/problem/counting-universal-subarrays/
