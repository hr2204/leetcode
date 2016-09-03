# 107. Binary Tree Level Order Traversal II
# Difficulty: Easy
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
#  (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        queue = []
        queue.append(root)
        while queue:
            tempQueue = []
            tempList = []
            for node in queue:
                tempList.append(node.val)
                if node.left:
                    tempQueue.append(node.left)
                if node.right:
                    tempQueue.append(node.right)
            queue = tempQueue
            res.insert(0,tempList)
        return res


if __name__ == '__main__':
    root = build_tree([1,3,4,4])
    printTree(root)
    print Solution().levelOrderBottom(root)