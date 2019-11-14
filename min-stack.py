# coding: utf-8

class MinStack(object):
    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.mins = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if self.mins and (number > self.mins[-1]):
            self.mins.append(self.mins[-1])
        else:
            self.mins.append(number)

    def pop(self):
        # pop and return the top item in stack
        if self.stack:
            self.mins.pop()
            return self.stack.pop()

    def min(self):
        # return the minimum number in stack
        if self.mins:
            return self.mins[-1]

# medium: http://lintcode.com/zh-cn/problem/min-stack/
