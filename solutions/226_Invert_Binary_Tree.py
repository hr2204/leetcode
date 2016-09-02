# -*- coding: utf-8 -*-
# 226. Invert Binary Tree
# Difficulty: Easy
# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root
    def helper(self,root):
        root.left, root.right = root.right, root.left
        if root.left:
            self.helper(root.left)
        if root.right:
            self.helper(root.right)

if __name__ == '__main__':
    root = build_tree([4,2,7,1,3,6,9])
    Solution().invertTree(root)
    printTree(root)
