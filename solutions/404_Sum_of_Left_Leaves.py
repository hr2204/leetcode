# 404. Sum of Left Leaves
# Difficulty: Easy
# Contributors: Admin
# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree, build_tree


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.helper(root, res)
        return sum(res)

    def helper(self, root, res):
        if not root:
            return

        if root.left:
            if not root.left.left and not root.left.right:
                res.append(root.left.val)
            self.helper(root.left, res)

        if root.right:
            self.helper(root.right, res)


if __name__ == '__main__':
    root = build_tree([3, 9, 20, None, None, 15, 7])
    printTree(root)
    print Solution().sumOfLeftLeaves(root)
