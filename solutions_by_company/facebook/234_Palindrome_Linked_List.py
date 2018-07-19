# 234. Palindrome Linked List
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        print temp
        reverted = self.revertLinkedList(head)

        idx = 0
        res = True
        while reverted:
            if reverted.val != temp[idx]:
                res = False
                break
            else:
                reverted = reverted.next
                idx += 1
        return res

    def revertLinkedList(self, head):

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

