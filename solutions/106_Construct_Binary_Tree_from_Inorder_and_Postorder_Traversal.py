# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Medium
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(postorder.pop())
            root = TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index + 1:],postorder )
            root.left = self.buildTree(inorder[:index],postorder)
            return root
if __name__ == '__main__':
    root = Solution().buildTree([1,2,3,4],[1,4,3,2])
    printTree(root)