# 328. Odd Even Linked List
# Difficulty: Medium
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(0)
        odd_head = odd
        even = ListNode(0)
        even_head = even
        isOdd = True
        while head:
            if isOdd:
                odd.next = head
                odd = odd.next
                isOdd = False
            else:
                even.next = head
                even = even.next
                isOdd = True
            head = head.next

        if isOdd:
            odd.next = None
        else:
            even.next = None
        odd.next = even_head.next
        return odd_head.next


if __name__ == "__main__":
    a = generate_list([1,2,3,4,5])

    head = Solution().oddEvenList(a)
    printNode(head)