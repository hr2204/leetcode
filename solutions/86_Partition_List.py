# 86. Partition List
# Difficulty: Medium
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = ListNode(0)
        new_head = left
        right = ListNode(0)
        mid = right
        pre = ListNode(0)
        while head:
            if head.val<x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
            if not head:
                left.next = mid.next
                right.next = None
        return new_head.next

        # return new_head.next




if __name__ == '__main__':
    a = generate_list([1,4,3,2,5,2])

    head = Solution().partition(a,3)
    printNode(head)