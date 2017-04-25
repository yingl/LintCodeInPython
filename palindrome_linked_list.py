# coding: utf-8

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        '''
        0->1->2->3->2->1->0 => 0->1->2, 3, 2->1->0
        0->1->2->3->3->2->1->0 => 0->1->2->3, 3->2->1->0
        '''
        if head:
            list_len = self.listLen(head)
            prev, slow, fast = None, head, head # fast每次前进2步
            while fast:
                fast = fast.next
                if not fast:
                    break
                fast = fast.next
                prev = slow
                slow = slow.next
            if list_len == 1:
                return True
            if (list_len % 2) == 1:
                # 长度为奇数
                old_tail = prev
                new_head = slow.next
            else:
                old_tail = prev
                new_head = prev.next
            old_tail.next = None
            new_head = self.reverse(new_head)
            while head and new_head:
                if head.val != new_head.val:
                    return False
                head = head.next
                new_head = new_head.next
        return True


    def reverse(self, head):  # 复制，而不是单纯反转。
        # write your code here
        if not head:
            return None
        new_head = None
        while head:
            node = ListNode(head.val)
            head = head.next
            node.next = new_head
            new_head = node
        return new_head

    def listLen(self, head):
        _len = 0
        while head:
            _len += 1
            head = head.next
        return _len

# medium: http://lintcode.com/problem/palindrome-linked-list
