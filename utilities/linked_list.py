from data_structure.list_node import ListNode

def printNode(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print "->".join(res)
def generate_list(nums):
    head = ListNode(0)
    curr = head
    for i in xrange(len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next

    return head.next


if __name__ == '__main__':
    print "listNode"


