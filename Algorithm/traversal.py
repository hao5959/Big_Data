class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #insert node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    #print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
    #inorder traversal
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
        return res

    #preorder
    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorder(root.left)
            res += self.preorder(root.right)
        return res
    
    #postorder
    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res += self.postorder(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
print(root.preorder(root))
print(root.postorder(root))