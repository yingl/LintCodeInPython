# coding: utf-8

class Solution:
    # @param {string} path the original path
    # @return {string} the simplified path
    def simplifyPath(self, path):
        # Write your code here
        dirs = path.split('/')
        new_path = []
        for _dir in dirs:
            if (_dir == '..') and (len(new_path) > 0):
                new_path.pop(-1)
            elif _dir and (_dir != '.') and (_dir != '..'):
                new_path.append(_dir)
        return '/' + '/'.join(new_path)

# medium: http://lintcode.com/zh-cn/problem/simplify-path/
