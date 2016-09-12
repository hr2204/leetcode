# 222. Count Complete Tree Nodes
# Difficulty: Medium
# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h
# nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
from math import pow
class Solution(object):

    class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if self.getDepth(root, True) == self.getDepth(root, False):  # True:isLeft
            return int(pow(2, self.getDepth(root, True))) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def getDepth(self, root, isLeft):
        level = 0

        while root:
            if isLeft:
                root = root.left
            else:
                root = root.right

            level += 1

        return level


    #TLE
    def countNodes_TLE(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        if not root:
            return count
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count

if __name__ == '__main__':
    root = build_tree([4,2,7,1,3,6,9,5,6])
    printTree(root)
    print Solution().countNodes(root)
