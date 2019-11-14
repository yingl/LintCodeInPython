class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.queue = []
        self.start = 0
        self.total = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        self.total += val
        if len(self.queue) == self.size: # 限制数组大小，实现更优雅。
            self.total -= self.queue[self.start]
            self.queue[self.start] = val
            self.start += 1
            self.start %- self.size
        else:
            self.queue.append(val)
        return self.total / len(self.queue)

# medium: https://lintcode.com/zh-cn/problem/moving-average-from-data-stream/
