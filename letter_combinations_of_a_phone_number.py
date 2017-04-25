# coding: utf-8

class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        # Write your code here
        if not digits:
            return []
        key_map = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        level = ['']
        i = 0
        while i < len(digits):
            pos = int(digits[i]) - 2
            if pos >= 0:
                new_level = []
                for comb in level:
                    for ch in key_map[pos]:
                        new_level.append(comb + ch)
                level = new_level
            i += 1
        return level

# medium: http://lintcode.com/zh-cn/problem/letter-combinations-of-a-phone-number/
