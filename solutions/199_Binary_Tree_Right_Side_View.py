# 199. Binary Tree Right Side View
# Difficulty: Medium
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        tmp = self.levelOrderTraversal(root)
        for i in tmp:
            res.append(i[-1])
        return res

    def levelOrderTraversal(self,root):
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while queue:
            tmpQueue = []
            tempRes= []
            for node in queue:
                tempRes.append(node.val)
                if node.left:
                    tmpQueue.append(node.left)
                if node.right:
                    tmpQueue.append(node.right)
            res.append(tempRes)
            queue = tmpQueue
        return res


if __name__ == '__main__':
    root = build_tree([1,2,3,4,5,6,7])
    printTree(root)
    print Solution().rightSideView(root)