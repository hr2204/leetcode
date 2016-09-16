# 103. Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = []
        reverFlag = False
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
            if not reverFlag:
                res.append(tempList)
                reverFlag = True
            else:
                reverFlag = False
                tempList.reverse()
                res.append(tempList)
            queue = tempQueue
        return res



if __name__ == '__main__':
    root = build_tree([1,2,3,4,5,6,7])
    root = build_tree([3,9,20,None,None,15,7])
    printTree(root)
    print Solution().zigzagLevelOrder(root)
