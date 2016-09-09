# 98. Validate Binary Search Tree
# Difficulty: Medium
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.hepler(root,res)
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False

        return True

    def hepler(self,root,res):
        if not root:
            return
        self.hepler(root.left,res)
        res.append(root.val)
        self.hepler(root.right,res)


if __name__ == '__main__':
    root = build_tree([1,3,4,4])
    printTree(root)
    print Solution().isValidBST(root)
    root = build_tree([2,1,3])
    printTree(root)
    print Solution().isValidBST(root)