# coding: utf-8

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        head = None
        tail = None
        flag = 0
        while (l1 is not None) and (l2 is not None):
            node = ListNode(l1.val + l2.val + flag)
            if node.val >= 10:
                flag = 1
                node.val %= 10
            else:
                flag = 0
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
            l1 = l1.next
            l2 = l2.next
        l3 = l1 if l1 is not None else l2
        while l3 is not None:
            node = ListNode(l3.val + flag)
            if node.val >= 10:
                flag = 1
                node.val %= 10
            else:
                flag = 0
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
            l3 = l3.next
        if flag:
            tail.next = ListNode(flag)
        return head

# easy: http://lintcode.com/zh-cn/problem/add-two-numbers/
