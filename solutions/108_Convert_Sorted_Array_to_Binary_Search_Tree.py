# 108. Convert Sorted Array to Binary Search Tree
# Difficulty: Medium
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)<1:
            return
        start,end = 0,len(nums)
        mid = (start + end)/2
        root = TreeNode(nums[mid])
        leftList = nums[start:mid]
        rightList = nums[mid+1:end]
        print leftList,rightList
        if len(leftList)>0:
            root.left = self.sortedArrayToBST(leftList)
        if len(rightList)>0:
            root.right = self.sortedArrayToBST(rightList)
        return root


if __name__ == '__main__':
    root = Solution().sortedArrayToBST([1,2,3,4,5,6])
    printTree(root)
