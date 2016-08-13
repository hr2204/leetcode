# 24. Swap Nodes in Pairs
# Difficulty: Easy
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None:
            return head
        last = ListNode(0)
        newHead = head.next
        cur = head
        while cur and cur.next:
            next = cur.next.next
            last.next = cur.next
            cur.next.next = cur
            cur.next = None
            last = cur
            cur = next
            if next is not None and next.next is None:
                last.next = next
        return newHead


if __name__ == "__main__":
    a = generate_list([1])
    head = Solution().swapPairs(a)
    printNode(head)