from squeue import *


# 二叉树的节点类
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 二叉树类,进行遍历操作
class Bitree():
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def preOrder(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node is None:
            return
        self.preOrder(node.left)
        print(node.data, end=" ")
        self.preOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return
        self.preOrder(node.left)
        self.preOrder(node.right)
        print(node.data, end=" ")

    # 层次遍历
    def levelOrder(self, node):
        qu = SQueue()
        qu.enqueue(node)
        while not qu.is_empty():
            node = qu.dequeue()
            print(node.data)
            if node.left is not None:
                qu.enqueue(node.left)
            if node.right is not None:
                qu.enqueue(node.right)



if __name__ == "__main__":
    # 按照后续遍历增加节点
    b = TreeNode("B")
    f = TreeNode("F")
    g = TreeNode("G")
    d = TreeNode("D", f, g)
    i = TreeNode("I")
    h = TreeNode("H")
    e = TreeNode("E", i, h)
    c = TreeNode("C", d, e)
    a = TreeNode("A", b, c)  # 跟节点

    bt = Bitree(a)  # 初始化树对象，传入跟节点
    print("pre order......")
    bt.preOrder(bt.root)
