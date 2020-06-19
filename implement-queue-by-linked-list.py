class MyQueue:
    def __init__(self):
        # 使用系统定义的ListNode
        self.head, self.tail = None, None

    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        # write your code here
        if not self.head:
            self.head = ListNode(item)
            self.tail = self.head
        else:
            self.tail.next = ListNode(item)
            self.tail = self.tail.next

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        ret = None
        if self.head:
            ret = self.head.val
            self.head = self.head.next
        return ret
        
# easy: https://www.lintcode.com/problem/implement-queue-by-linked-list/
