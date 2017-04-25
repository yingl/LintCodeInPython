# coding: utf-8

class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        ret = []
        word_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in word_map:
                word_map[sorted_word] = {'count':1, 'words':[word]}
            else:
                word_map[sorted_word]['count'] += 1
                word_map[sorted_word]['words'].append(word)
        for key, info in word_map.items():
            if info['count'] > 1:
                for word in info['words']:
                    ret.append(word)
        return ret

# medium: http://lintcode.com/zh-cn/problem/anagrams/
