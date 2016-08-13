# 203. Remove Linked List Elements
# Difficulty: Easy
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        p = dummyNode
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummyNode.next
if __name__ == "__main__":
    a = generate_list([1,1, 2, 2, 4])
    head = Solution().removeElements(a,4)
    printNode(head)