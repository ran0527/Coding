"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        # visited = set()
        # i = head
        # while i:
        #     if i in visited:
        #         return True
        #     visited.add(i)
        #     i = i.next
        # return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


    # def hasDuplciate(self, array):
    #     for i in range(len(array)):
    #         for j in range(i + 1, len(array), 1):
    #             if i == j
    #                 return True
    #     return False
