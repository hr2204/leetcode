# 234. Palindrome Linked List
# Difficulty: Easy
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        orgin = list()
        p0 = head
        while head:
            orgin.append(head.val)
            head = head.next
        head = self.reverseList(p0)
        i = 0
        printNode(head)
        while head:
            if head.val!=orgin[i]:
                return False
            head = head.next
            i += 1
        return True

    def reverseList(self,head):
        if head is None:
            return
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

if __name__ == "__main__":
    a = generate_list([1,2,3,1])
    print Solution().isPalindrome(a)


