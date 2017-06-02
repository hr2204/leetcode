# 515. Find Largest Value in Each Tree Row
# Difficulty: Medium
# Contributors:
# love_Fawn
# You need to find the largest value in each row of a binary tree.
#
# Example:
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            cur_row = []
            cur_row_val = []
            for node in queue:
                cur_row_val.append(node.val)
                if node.left:
                    cur_row.append(node.left)
                if node.right:
                    cur_row.append(node.right)
            res.append(max(cur_row_val))
            queue = cur_row
        return res

if __name__ == '__main__':
    head = build_tree([1,3,2,5,3,"",9])
    printTree(head)
    print Solution().largestValues(head)

