# 94. Binary Tree Inorder Traversal
# Difficulty: Medium
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        if not root:
            return res

        self.helper(root,res)
        return res

    def helper(self,root,res):
        if not root:
            return
        self.helper(root.left,res)
        res.append(root.val)
        self.helper(root.right,res)


if __name__ == '__main__':
    root = build_tree([1,3,4,4])
    printTree(root)
    print Solution().inorderTraversal(root)