# 141. Linked List Cycle
# Difficulty: Easy
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        fast = head.next.next
        slow = head.next
        while fast:
            if fast == slow:
                return True
            if fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return False
