# 21. Merge Two Sorted Lists
# Difficulty: Easy
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            newHead = l1
            l1 = l1.next
        else:
            newHead = l2
            l2 = l2.next
        res = newHead
        while l1 and l2:
            if l1.val <= l2.val:
                newHead.next = l1
                l1 = l1.next
            else:
                newHead.next = l2
                l2 = l2.next
            newHead = newHead.next
        if l1 is None:
            newHead.next = l2
        else:
            newHead.next = l1

        return res


if __name__ == "__main__":
    a = generate_list([1,1, 2, 2, 4])
    b = generate_list([1,3, 4, 5])

    head = Solution().mergeTwoLists(a,b)
    printNode(head)