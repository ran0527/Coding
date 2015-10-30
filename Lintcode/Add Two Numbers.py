# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        result = dummy
        carry = 0
    while l1 or l2 or carry:
            if l1 == None and l2 == None:
                result.next = ListNode(carry)
                result = result.next
                carry = 0
            elif l1 == None:
                result.next = ListNode(l2.val + carry)
                l2 = l2.next
                result = result.next
                carry = 0
            elif l2 == None:
                result.next = ListNode(l1.val + carry)
                l1 = l1.next
                result = result.next
                carry = 0
            else:
                result.next = ListNode((l1.val + l2.val + carry) % 10)
                carry = (l1.val + l2.val + carry)//10
                l1 = l1.next
                l2 = l2.next
                result = result.next
        return dummy.next
