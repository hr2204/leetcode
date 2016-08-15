# 160. Intersection of Two Linked Lists
# Difficulty: Easy
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return
        p1, p2 = headA, headB
        lenA, lenB = 1, 1
        while p1:
            p1 = p1.next
            lenA += 1
        while p2:
            p2 = p2.next
            lenB += 1
        n = lenA - lenB
        p1, p2 = headA, headB
        if n>0:
            while n:
                p1 = p1.next
                n -= 1
        else:
            n *= -1
            while n:
                p2 = p2.next
                n -= 1

        while p1:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next
        return None
if __name__ == "__main__":
    a = generate_list([1,1, 2, 2, 4])
    head = Solution().deleteDuplicates(a)
    printNode(head)