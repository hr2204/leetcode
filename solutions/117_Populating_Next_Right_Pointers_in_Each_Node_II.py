# 117. Populating Next Right Pointers in Each Node II
# Difficulty: Medium
# Contributor: LeetCode
# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        queue = list()
        queue.append(root)

        while queue:
            tempQueue = list()
            for i in range(len(queue)):
                if i == len(queue) -1:
                    queue[i].next = None

                else:
                    queue[i].next = queue[i+1]

                if queue[i].left:
                    tempQueue.append(queue[i].left)
                if queue[i].right:
                    tempQueue.append(queue[i].right)
            queue = tempQueue

if __name__ == '__main__':
