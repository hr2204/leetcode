from data_structure.tree_node import TreeNode

def build_tree(nums):
    if not nums:
        return None

    root = TreeNode(nums.pop(0))

    stack = [root]
    while stack and nums:
        new_stack = []
        for i in xrange(len(stack)):
            if len(nums) <= 0:
                return root
            else:
                if nums[0]:
                    left = TreeNode(nums.pop(0))
                    stack[i].left = left
                    new_stack.append(left)
                else:
                    nums.pop(0)
            if len(nums) <= 0:
                return root
            else:
                if nums[0]:
                    right = TreeNode(nums.pop(0))
                    stack[i].right = right
                    new_stack.append(right)
                else:
                    nums.pop(0)

        stack = new_stack

    return root


def generateTree(treeList):
    root = TreeNode("")
    queue = list()
    queue.append(root)
    while len(treeList)>0:
        node = queue[0]
        queue.pop(0)
        node.val = treeList[0]
        treeList.pop(0)
        node.left = TreeNode("")
        node.right= TreeNode("")
        queue.append(node.left)
        queue.append(node.right)

    return root


# root = build_tree([1,2,3,4,5,6])


def printTree(root):
    queue = list()
    queue.append(root)
    res = []
    while queue:
        rowVal = []
        tmpRow = []
        for node in queue:
            if node:
                rowVal.append(node.val)
                tmpRow.append(node.left)
                tmpRow.append(node.right)
        queue = tmpRow
        if rowVal:
            res.append(rowVal)
    for i in res:
        print i


def printTree_1(head):

    queue = list()
    queue.append(head)
    while len(queue)>0:
        cur = queue[0]
        if cur.val!="":
            print cur.val
        queue.pop(0)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)

# printTree(root)
# for i in res:
#     print i