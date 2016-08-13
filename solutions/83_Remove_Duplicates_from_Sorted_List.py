# 83. Remove Duplicates from Sorted List
# Difficulty: Easy
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        tmp = head
        while tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head
if __name__ == "__main__":
    a = generate_list([1,1, 2, 2, 4])
    head = Solution().deleteDuplicates(a)
    printNode(head)
