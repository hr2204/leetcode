# 116. Populating Next Right Pointers in Each Node
# Difficulty: Medium
# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL


# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return

        queue = list()
        queue.append(root)

        while queue:
            tempQueue = list()
            for i in range(len(queue)):
                if i == len(queue) -1:
                    queue[i].next = None

                else:
                    queue[i].next = queue[i+1]

                if queue[i].left:
                    tempQueue.append(queue[i].left)
                if queue[i].right:
                    tempQueue.append(queue[i].right)
            queue = tempQueue

if __name__ == '__main__':
    root = build_tree([1,2,3,4,5,6,7])
    printTree(root)
    Solution().connect(root)
    printTree(root)