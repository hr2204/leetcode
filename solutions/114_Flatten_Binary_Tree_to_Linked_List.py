# 114. Flatten Binary Tree to Linked List
# Difficulty: Medium
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# click to show hints.
#
# Hints:
# If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        list = []
        self.preOrderTraversal(root,list)
        for i in range(len(list)-1):
            list[i].right = list[i+1]
            list[i].left = None
    def preOrderTraversal(self,root,list):
        list.append(root)
        if root.left:
            self.preOrderTraversal(root.left,list)
        if root.right:
            self.preOrderTraversal(root.right,list)



if __name__ == '__main__':
    root = build_tree([1,2,5,3,4,None,6])
    printTree(root)
    Solution().flatten(root)
    printTree(root)
