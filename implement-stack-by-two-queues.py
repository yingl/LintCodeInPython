class Queue:
    def __init__(self):
        self.i = 0
        self.arr = []

    def push(self, v):
        self.arr.append(v)

    def pop(self):
        r = self.arr[self.i]
        self.i += 1
        return r

    def top(self):
        return self.arr[self.i]

    def is_empty(self):
        return len(self.arr) == self.i

class Stack:
    def __init__(self):
        self.qs= [Queue(), Queue()]
        self.flag = 0

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        nf = 1 - self.flag
        self.qs[nf].push(x)
        while not self.qs[self.flag].is_empty():
            self.qs[nf].push(self.qs[self.flag].pop())
        self.flag = nf


    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        return self.qs[self.flag].pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.qs[self.flag].top()

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.qs[self.flag].is_empty()
      
# easy: https://www.lintcode.com/problem/494/
