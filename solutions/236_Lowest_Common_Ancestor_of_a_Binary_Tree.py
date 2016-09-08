# -*- coding: utf-8 -*-
# 236. Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
# two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a
# node to be a descendant of itself).”
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
# since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if root == p or root == q:
            return root
        list1,list2 = [],[]
        self.getLeafToRootPath(root,p,list1)
        self.getLeafToRootPath(root,q,list2)
        if q in list1:
            return q
        if p in list2:
            return p
        print list1
        print list2

        for node in list1:
            if node in list2:
                return node



    def getLeafToRootPath(self,root,node,path):
        if not root:
            return False
        if root == node or self.getLeafToRootPath(root.left,node,path) or self.getLeafToRootPath(root.right,node,path):
            path.append(root)
            return True
        return False


if __name__ == '__main__':
    root = build_tree([3,5,1,6,2,0,8,"","",7,4])
    printTree(root)
    # print Solution().isContainNode(root,k)
    p = root.left.left #6
    q = root.left.right.left #7
    list = []
    Solution().getLeafToRootPath(root,p,list)
    print list
    for node in list:
        print node.val
    print Solution().lowestCommonAncestor(root,p,q).val #5