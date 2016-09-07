# 129. Sum Root to Leaf Numbers
# Difficulty: Medium
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        pathSum = 0
        if not root:
            return 0
        self.helper(root,res,pathSum)
        return sum(res)

    def helper(self,root,res,pathSum):
        if not root.left and not root.right:
            res.append( pathSum * 10 + root.val)
        else:
            pathSum = pathSum * 10 + root.val
            if root.left:
                self.helper(root.left,res,pathSum)
            if root.right:
                self.helper(root.right,res,pathSum)





if __name__ == '__main__':
    root = build_tree([1,2,3,4,5,6,7])
    printTree(root)
    print Solution().sumNumbers(root)