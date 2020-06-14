class Node:
    """
    This class represents structure of a particular node in binary tree
    Every node has atmost 2 children and a key
    """
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def traverse_breadth_first(root):
    """
    This function prints the breadth first order traversal of a binary tree i.e it traverses thetree level-by-level
    :param root: root node of the binary tree
    """
    if root is None:
        return

    lis = []
    lis.append(root)

    while(len(lis)>0):
        print(lis[0].data)

        node = lis.pop(0)

        #check for the left and right nodes
        if node.left is not None:
            lis.append(node.left)

        if node.right is not None:
            lis.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Level order traversal of binary tree is ")
    traverse_breadth_first(root)