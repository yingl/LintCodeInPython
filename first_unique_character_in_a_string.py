class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        # a ~ z = 65 ~ 90
        # A ~ Z = 97 ~ 122
        # 122 - 65 + 1 = 58
        data = [0] * 58 # 计数统计
        for c in str:
            data[ord(c) - 65] += 1
        for c in str: # 看首先出现次数为1的就返回
            if data[ord(c) - 65] == 1:
                return c
                
# easy: https://www.lintcode.com/problem/first-unique-character-in-a-string
