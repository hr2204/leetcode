# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structure.tree_node import TreeNode
from utilities.tree_operations import printTree,build_tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if not self.check(node):
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True
    def check(self, root):

        if not root:
            return True
        print self.maxDepth(root.left), self.maxDepth(root.right)
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right))<=1
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        depth = 0
        if not root:
            return depth
        else:
            return self.helper(root,depth)

    def helper(self,node,depth):
        depth += 1
        if not node.left and not node.right:
            return depth
        if node.left and node.right:
            return max(self.helper(node.left,depth),self.helper(node.right,depth))
        if node.left:
            return self.helper(node.left,depth)
        if node.right:
            return self.helper(node.right,depth)




if __name__ == '__main__':
    root = build_tree([1,None,2,None,3])
    printTree(root)
    print Solution().isBalanced(root)