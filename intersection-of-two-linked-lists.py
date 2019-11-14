# coding: utf-8

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        list_a_len = self.listLen(headA)
        list_b_len = self.listLen(headB)
        steps = abs(list_a_len - list_b_len)
        for i in xrange(steps):
            if list_a_len > list_b_len:
                headA = headA.next
            else:
                headB = headB.next
            i += 1
        while True:
            if headA != headB:
                headA = headA.next
                headB = headB.next
            else:
                return headA

    def listLen(self, head):
        list_len = 0
        while head:
            list_len += 1
            head = head.next
        return list_len

# medium: http://lintcode.com/zh-cn/problem/intersection-of-two-linked-lists/
