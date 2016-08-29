from data_structure.tree_node import TreeNode

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

def generateTree(nums):
    stack =[]
    while len(nums)>0:
        node = queue[0]
        queue.pop(0)
        node.val = treeList[0]
        treeList.pop(0)
        node.left = TreeNode("")
        node.right= TreeNode("")
        queue.append(node.left)
        queue.append(node.right)

    return root

root = generateTree([1,2,3,4,5,6])


def printTree(root):
    queue = list()
    queue.append(root)
    res = []
    while queue:
        rowVal = []
        tmpRow = []
        for node in queue:
            rowVal.append(node.val)
            tmpRow.append(node.left)
            tmpRow.append(node.right)
        queue = tmpRow
        res.append(rowVal)
    return res


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

printTree(root)