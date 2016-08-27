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


root = generateTree([1,2,3,4,5,6])

def printTree(head):

    queue = list()
    queue.append(head)
    while len(queue)>0:
        cur = queue[0]
        if cur.val!="":
            print cur.val
        queue.pop(0)
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)

printTree(root)