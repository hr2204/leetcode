 # 145. Binary Tree Postorder Traversal
# Difficulty: Hard
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        if not root:
            return res

        self.helper(root,res)
        return res

    def helper(self,root,res):
        if not root:
            return
        self.helper(root.left,res)
        self.helper(root.right,res)
        res.append(root.val)