# 257. Binary Tree Paths
# Difficulty: Easy
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):

        res = []
        if not root:
            return res
        path = str(root.val)
        if root.left:
            self.helper(root.left,path,res)
        if root.right:
            self.helper(root.right,path,res)
        if root.left is None and root.right is None:
            res.append(path)

        return res

    def helper(self,node,path,res):
        path += "->" + str(node.val)
        if node.left is None and node.right is None:
            res.append(path)
        if node.left:
            self.helper(node.left,path,res)
        if node.right:
            self.helper(node.right,path,res)


if __name__ == '__main__':
    head = build_tree([1])
    printTree(head)
    print Solution().binaryTreePaths(head)