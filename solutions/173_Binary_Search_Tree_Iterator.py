# 173. Binary Search Tree Iterator
# Difficulty: Medium
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
from math import pow

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.list = []
        self.index = -1
        self.inorderTraversal(root,self.list)

    def inorderTraversal(self,root,list):
        if not root:
            return
        self.inorderTraversal(root.left,list)
        list.append(root.val)
        self.inorderTraversal(root.right,list)


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index<len(self.list)-1:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.list[self.index]


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

if __name__ == '__main__':
    root = build_tree([4,2,7,1,3,6,9,5,6])
    printTree(root)
    i, v = BSTIterator(root), []
    print i.list
    while i.hasNext():
        v.append(i.next())
    print v
