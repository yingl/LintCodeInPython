class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        # write your code here
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        ret.reverse()
        return ret

# easy: https://www.lintcode.com/problem/reverse-order-storage
