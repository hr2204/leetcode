# 82. Remove Duplicates from Sorted List II
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 106396
# Total Submissions: 364865
# Difficulty: Medium
# Contributor: LeetCode
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

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
        if not head:
            return
        cur = head
        node_map = {}
        while cur:
            if cur.val not in node_map:
                node_map[cur.val] = 1
            else:
                node_map[cur.val] += 1
            cur = cur.next

        print node_map
        dummy = ListNode(0)
        temp = dummy
        cur = head
        node_list = []
        while cur:
            if node_map[cur.val] == 1:
                node_list.append(cur)
            cur = cur.next

        if node_list:
            node_list[-1].next = None

        for node in node_list:
            temp.next = node
            temp = node

        return dummy.next


if __name__ == '__main__':
    a = generate_list([1, 2, 2])
    printNode(a)
    head = Solution().deleteDuplicates(a)
    printNode(head)
