# 206. Reverse Linked List
# Difficulty: Easy
# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next

        return pre


if __name__ == "__main__":
    a = generate_list([1, 2, 3])
    head = Solution().reverseList(a)
    printNode(head)
