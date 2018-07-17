# 206. Reverse Linked List
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return

        if not head.next:
            return head

        pre = head
        cur = head.next
        pre.next = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    node = Solution().reverseList(head)

    while node:
        print node.val
        node = node.next
