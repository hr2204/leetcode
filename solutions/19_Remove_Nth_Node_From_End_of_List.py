# 19. Remove Nth Node From End of List
# Difficulty: Easy
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return
        len = 0
        dummyNode = ListNode(0)
        dummyNode.next = head
        p1 = dummyNode
        while p1:
            p1 = p1.next
            len += 1
        n = len - n -1
        p1 = dummyNode
        if n == 0:
            return head.next
        while n > 0:
            p1 = p1.next
            n -= 1
        p1.next = p1.next.next
        return head

if __name__ == "__main__":
    a = generate_list([1,2,3,4])
    head = Solution().removeNthFromEnd(a,4)
    printNode(head)