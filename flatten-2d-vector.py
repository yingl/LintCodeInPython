class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.row, self.col = 0, 0
        while (self.row < len(self.vec2d)) \
              and (self.col >= len(self.vec2d[self.row])):
            self.row += 1
            self.col = 0 # 处理空数组特殊情况
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        i = self.vec2d[self.row][self.col]
        self.col += 1
        while (self.row < len(self.vec2d)) \
              and (self.col >= len(self.vec2d[self.row])):
            self.row += 1
            self.col = 0 # 再次处理空数组特殊情况
        return i

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        return (self.row < len(self.vec2d)) and (self.col < len(self.vec2d[self.row]))

# medium: https://www.lintcode.com/problem/flatten-2d-vector/
