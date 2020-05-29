class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        if len(self.stack) <= self.size:
            self.stack.append(x)
        else:
            self.stack[self.size] = x
        self.size += 1

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.size -= 1
        return self.stack[self.size];

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[self.size -1];

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.size == 0

# easy: https://www.lintcode.com/problem/implement-stack/
