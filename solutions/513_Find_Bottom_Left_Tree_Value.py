# 513. Find Bottom Left Tree Value
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 16303
# Total Submissions: 29211
# Difficulty: Medium
# Contributors:
# abhijeet17
# Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
# Example 2:
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = []
        queue.append(root)
        while queue:
            temp_val = []
            cur_row = []
            for node in queue:
                temp_val.append(node.val)
                if node.left:
                    cur_row.append(node.left)
                if node.right:
                    cur_row.append(node.right)
            queue = cur_row
        return temp_val[0]



if __name__ == '__main__':
    head = build_tree([2,1,3,"",3])
    printTree(head)
    print Solution().findBottomLeftValue(head)