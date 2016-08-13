from data_structure.list_node import ListNode
from utilities.linked_list import generate_list, printNode



if __name__ == "__main__":
    a = generate_list([1,1, 2, 2, 4])
    head = Solution().deleteDuplicates(a)
    printNode(head)