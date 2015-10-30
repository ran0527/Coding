"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        n = n + 1
        count = 0
        cur = head
        while cur != None:
            cur = cur.next
            count += 1
        k = count - n
        cur = head
        if k == -1:
            return head.next
        while k != 0:
            k -= 1
            cur = cur.next
        cur.next = cur.next.next
        return head
