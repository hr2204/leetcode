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
        if inorder:
            index = inorder.index(preorder[0])
            del preorder[0]
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root


if __name__ == '__main__':
    root = Solution().buildTree([1,4,2,3],[1,2,3,4])
    printTree(root)
