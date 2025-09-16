from markdown_it.rules_core.normalize import NULL_RE

class Node:
    value=None
    left = None
    right = None
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

    def depth_first_search(self, tree, value):
        if tree==None:
            return None
        if tree.value==value:
            return tree
        tleft = self.depth_first_search(tree.left, value)
        tright = self.depth_first_search(tree.right, value)
        if not tleft==None:
            return tleft
        if not tright==None:
            return tright
        return None
    def print(self, node):
        if node==None:
            return
        print("node_value=",node.value, node.left, node.right)
        self.print(node.left)
        self.print(node.right)

if __name__=="__main__":
    node_left = Node(10)
    node_right = Node(12)
    node_left_2 = Node(9)
    node_right_2 = Node(8)

    node_left_a = Node(8, left=node_left, right=node_right)
    node_right_a = Node(6, left=node_left_2, right=node_right_2)
    node = Node(4, left=node_left_a, right = node_right_a)
    node.print(node)
    a = node.depth_first_search(node, 6)
    print("rez",a.value)


