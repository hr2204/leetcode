# 101. Symmetric Tree
# Difficulty: Easy
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root.left,root.right)
    def helper(self,leftNode,rightNode):
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None and rightNode is not None:
            return False
        if leftNode is not None and rightNode is None:
            return False
        if leftNode.val!=rightNode.val:
            return False
        return self.helper(leftNode.left,rightNode.right) and self.helper(leftNode.right,rightNode.left)

if __name__ == '__main__':
    head = build_tree([1,2,2,3,4,4,3])
    printTree(head)
    print Solution().isSymmetric(head)
