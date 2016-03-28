class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    # def __init__(self):
    #     self.value = None
    #     self.left_node = None
    #     self.right_node = None

    def __str__(self):
        s = ""
        s += self.left_node.__str__()
        s += str(self.value)
        s += self.right_node.__str__()
        return s

    def __repr__(self):
        return self.__str__()


class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def append(self, value):
        if (self.root_node == None):
            self.root_node = TreeNode(value)
        else:
            par = self.__find_parent(self.root_node, value)
            if (par.value < value):
                par.right_node = TreeNode(value)
            else:
                par.left_node = TreeNode(value)
        print self.root_node

    def __find_parent(self, node, value):
        if (node):
            if (node.value == value):
                return node
            elif (node.value > value):
                if (node.left_node):
                    return self.__find_parent(node.left_node, value)
                else:
                    return node
            elif (node.value < value):
                if (node.right_node):
                    return self.__find_parent(node.right_node, value)
                else:
                    return node

        return None

    def __find_node(self, node, value):
        found = self.__find_parent(node, value)
        if (found):
            if (found.value == value):
                return node

    def find(self, value):
        return self.__find_node(self.root_node, value)


tree = BinarySearchTree()
tree.append(5)
tree.append(4)
tree.append(8)
tree.append(10)
