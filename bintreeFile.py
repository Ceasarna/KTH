class TreeNode:
    def __init__(self, value):
        self.val = value
        self.leftChild = None
        self.rightChild = None


class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        # In case the tree is empty; put the value as the root.
        if self.root is None:
            self.root = TreeNode(newvalue)
        # Recursive method that will call for _put which will organize.
        else:
            self._put(self.root, newvalue)

    def _put(self, node, value):
        # Puts the value to the left
        if value < node.val:
            if node.leftChild is not None:
                self._put(node.leftChild, value)
            else:
                node.leftChild = TreeNode(value)
        # Puts the value to the right
        else:
            if node.rightChild is not None:
                self._put(node.rightChild, value)
            else:
                node.rightChild = TreeNode(value)

    # Checks for the value in a Bintree
    def __contains__(self, value):
        if self.root is not None:
            return self._find(self.root, value)
        else:
            return None

    def _find(self, node, value):
        if node.val is value:
            return node
        elif node.val > value and node.leftChild is not None:
            self._find(node.leftChild, value)
        elif node.val < value and node.rightChild is not None:
            self._find(node.rightChild, value)

    def write(self):
        if self.root is not None:
            self._write(self.root)

    def _write(self, node):
        if node is not None:
            self._write(node.leftChild)
            print(node.val)
            self._write(node.rightChild)





tree = Bintree()
tree.put(3)
tree.put(4)
tree.put(0)
tree.put(8)
tree.put(2)
tree.write()
