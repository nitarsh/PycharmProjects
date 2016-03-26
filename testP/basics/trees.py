class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __str__(self):
        str = []
        str.append(self.left_node.__str__)
        str.append(self.value)
        str.append(self.right_node.__str__)

    def __repr__(self):
        return self.__str__()


class BinaryTree:
    def __init__(self):
        self.root_node = TreeNode()
