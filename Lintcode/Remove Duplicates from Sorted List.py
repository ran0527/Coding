"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head == None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head and head.next and head.next.next:
            if head.next.val == head.next.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next
