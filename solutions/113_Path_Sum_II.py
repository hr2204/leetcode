# 113. Path Sum II
# Difficulty: Medium
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        res = []
        tmpPath = []
        if not root:
            return res

        self.helper(root,res,tmpPath,sum)
        return res

    def helper(self,root,res,tmpPath,sum):
        tmpPath = tmpPath + [root.val]
        if root.val == sum and not root.left and not root.right:
            res.append(tmpPath)
        if root.left:
            self.helper(root.left,res,tmpPath,sum-root.val)
        if root.right:
            self.helper(root.right,res,tmpPath,sum-root.val)


if __name__ == '__main__':
    head = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    printTree(head)
    print Solution().pathSum(head,22)