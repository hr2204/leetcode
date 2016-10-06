# 2. Add Two Numbers
# Difficulty: Medium
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        # """
        pre = ListNode(0)
        dummy = pre
        carry = 0
        while l1 and l2:
            digit = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val + carry)/10
            pre.next = ListNode(digit)
            pre = pre.next
            l1 = l1.next
            l2 = l2.next
        tail = None
        if l1:
            tail = l1
        if l2:
            tail = l2
        while tail:
            digit = (tail.val + carry)%10
            carry = (tail.val + carry)/10
            pre.next = ListNode(digit)
            pre = pre.next
            tail = tail.next

        if carry:
            pre.next = ListNode(1)

        return dummy.next


if __name__ == '__main__':
    a = generate_list([1,8])
    b = generate_list([1,2,1])

    # reversed = Solution().reveser_list(a)
    # printNode(reversed)
    head = Solution().addTwoNumbers(a,b)
    printNode(head)