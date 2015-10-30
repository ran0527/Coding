"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        while l1 or l2:
            if l1 == None:
                tail.next = ListNode(l2.val)
                tail = tail.next
                l2 = l2.next
            elif l2 == None:
                tail.next = ListNode(l1.val)
                l1 = l1.next
                tail = tail.next
            else:
                if l1.val < l2.val:
                    tail.next = ListNode(l1.val)
                    l1 = l1.next
                    tail = tail.next
                else:
                    tail.next = ListNode(l2.val)
                    l2 = l2.next
                    tail = tail.next
        return dummy.next
