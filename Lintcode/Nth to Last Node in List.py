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
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        # write your code here
        count = 0
        cur = head
        while cur != None:
            cur = cur.next
            count += 1
        k = count - n
        cur = head
        while k != 0:
            k -= 1
            cur = cur.next
        return cur
        
