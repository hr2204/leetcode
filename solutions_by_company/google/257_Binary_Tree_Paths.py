# 257. Binary Tree Paths
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return []

        if root.left:
            for tmp in self.binaryTreePaths(root.left):
                res.append(str(root.val) + '->' + tmp)

        if root.right:
            for tmp in self.binaryTreePaths(root.right):
                res.append(str(root.val) + '->' + tmp)

        if not root.left and not root.right:
            res.append(str(root.val))

        return res

