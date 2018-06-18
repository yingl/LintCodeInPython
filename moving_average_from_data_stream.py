class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.queue = []
        self.start = 0 # 考虑到用list模拟queue的效率，还是空间换时间吧。
        self.total = float(0)

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.total += float(val)
        self.queue.append(val)
        if (len(self.queue) - self.start) > self.size:
            self.total -= self.queue[self.start]
            self.start += 1
        return self.total / (len(self.queue) - self.start)
