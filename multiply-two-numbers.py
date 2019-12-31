"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the product list of l1 and l2
    """
    def multiplyLists(self, l1, l2):
        # write your code here
        ret = 0
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        print(l1.val, l2.val)
        i = 1
        while l1:
            j = 1
            tmp = l2
            while tmp:
                ret += i * j * l1.val * tmp.val
                tmp = tmp.next
                j *= 10
            i *= 10
            l1 = l1.next
        return ret
                
    def reverse(self, node):
        head, tail = None, None
        while node:
            if not head:
                head, tail = node, node
                node = node.next
                tail.next = None
            else:
                tmp = node.next
                node.next = head
                head = node
                node = tmp
        return head

# easy: https://www.lintcode.com/problem/multiply-two-numbers/
