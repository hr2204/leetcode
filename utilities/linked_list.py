from data_structure.list_node import ListNode

def printNode(head):
    while head:
        print head.val
        head = head.next

def generate_list(nums):
    head = ListNode(0)
    curr = head
    for i in xrange(len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    return head.next


if __name__ == '__main__':
    print "listNode"


