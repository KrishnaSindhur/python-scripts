''' Binary search tree implementation'''


class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def binary_insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                binary_insert_node(root.left, node)
        elif root.data < node.data:
            if root.right == None:
                root.right = node
            else:
                binary_insert_node(root.right, node)


def level_order(root):

    queue = []
    queue.append(root)
    while (len(queue) > 0):
        node = queue.pop(0)
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def preorder_recursive(root):

    if not root:
        return
    print(root.data)
    preorder_recursive(root.left)
    preorder_recursive(root.right)


def inorder_recursive(root):

    if not root:
        return
    inorder_recursive(root.left)
    print(root.data)
    inorder_recursive(root.right)

def postorder_recursive(root):

    if not root:
        return
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    print(root.data)


r = Node(3)
binary_insert_node(r, Node(7))
binary_insert_node(r, Node(5))
binary_insert_node(r, Node(1))
level_order(r)
print("Preorder traversal:")
preorder_recursive(r)
print("Inorder traversal:")
inorder_recursive(r)
print("Postorder traversal:")
postorder_recursive(r)
