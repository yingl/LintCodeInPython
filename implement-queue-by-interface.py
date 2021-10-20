class InterfaceQueue:
    def push(self, element):
        pass

    # define an interface for pop method
    # write your code here
    def pop(self):
        pass

    # define an interface for top method
    # write your code here
    def top(self):
        pass

class MyQueue(InterfaceQueue):
    # you can declare your private attributes here
    def __init__(self):
        # do initialization if necessary
        self.i = 0
        self.data = []
		
    # implement the push method
    # write your code here
    def push(self, val):
        self.data.append(val)
		
    # implement the pop method
    # write your code here
    def pop(self):
        ret = self.data[self.i]
        self.i += 1
        return ret
    	
	# implement the top method
    # write your code here
    def top(self):
        return self.data[self.i]
        
# Your MyQueue object will be instantiated and called as such:
# MyQueue queue = new MyQueue();
# queue.push(123);
# queue.top(); will return 123;
# queue.pop(); will return 123 and pop the first element in the queue

# easy: https://www.lintcode.com/problem/546
