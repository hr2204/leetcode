#-*-coding:utf-8 -*-
# 143. Reorder List
# Difficulty: Medium
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        mid = head
        fast = head
        pre = head
        while fast and fast.next:
            pre = mid
            mid = mid.next
            fast = fast.next.next
        pre.next = None
        l2 = self.rever_list(mid)
        self.merge_list(head,l2)

    def rever_list(self,head):
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def merge_list(self,h1,h2):
        while h2 and h1:
            temp = h1.next
            temp2 = h2.next
            h1.next = h2
            h1.next.next = temp
            if not temp:
                h2.next = temp2
            h1 = temp
            h2 = temp2


if __name__ == "__main__":
    head = generate_list([1,2,3,4])

    # Solution().reorderList(head)
    res = Solution().reorderList(head)
    # printNode(head)
    printNode(res)