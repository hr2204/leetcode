# 61. Rotate List
# Difficulty: Medium
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        fast = head
        len = 0
        lenHead = head
        while lenHead:
            lenHead = lenHead.next
            len += 1
        if k > len:
            k = k%len
        if len == k or k == 0:
            return head

        print k
        while fast and k:
            fast = fast.next
            k -= 1
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head

if __name__ == "__main__":
    a = generate_list([1,2,3,4,5])

    head = Solution().rotateRight(a,5)
    printNode(head)
    a = generate_list([1])

    head = Solution().rotateRight(a,1)
    printNode(head)
