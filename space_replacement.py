# coding: utf-8

class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if string is None:
            return 0
        new_length = length
        for ch in string:
            if ch == ' ':
                new_length += 2 # 每个空格将多占2个空间
        index = new_length
        '''
        'ab cd '长度为6，替换后长度为10。
        从后往前遍历，根据是否空格调整index位置。
        '''
        for i in xrange(length - 1, -1, -1):
            if string[i] == ' ':
                index -= 3
                string[index: index + 3] = ['%', '2', '0']
            else:
                index -= 1
                string[index] = string[i]
        return len(string)

# easy: http://lintcode.com/zh-cn/problem/space-replacement/
