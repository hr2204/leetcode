# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# Given preorder and inorder traversal of a tree, construct the binary tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """


if __name__ == '__main__':
    root = Solution().buildTree([1,3,4,4])
    printTree(root)
