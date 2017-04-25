# coding: utf-8

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(element)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def top(self):
        # write your code here
        # return the top element
        if self.stack1:
            return self.stack1[-1]

    def pop(self):
        # write your code here
        # pop and return the top element
        return self.stack1.pop()

# medium: http://lintcode.com/zh-cn/problem/implement-queue-by-two-stacks/
