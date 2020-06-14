# Python program to find the nearest common parent nodes of k1 and k2

class Node:
    """
    This class represents structure of a particular node in binary tree
    Every node has atmost 2 children and a key
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def get_nearest_common_parent(root, k1, k2):
    """
    This function returns the nearest common parent of two given nodes assuming the two nodes are present in binary tree
    :param root: root node of the binary tree
    :param k1: key of node 1 of the binary tree whose common nearest parent has to be found
    :param k2: key of node 2
    :return: nearest common parent of k1 and k2
    """
    if (root is None):
        return None

    #if the root node's key is equal to k1 or k2, return root as the nearest common parent
    if (root.key == k1 or root.key == k2):
        return root

    #Look for keys in left and right sub trees
    left_common_node = get_nearest_common_parent(root.left, k1, k2)
    right_common_node = get_nearest_common_parent(root.right, k1, k2)

    #If left_common_node and right_common_node are not None here, then one node is present in left subtree
    #another node is present in right subtree, so this node is the nearest common parent
    if (left_common_node and right_common_node):
        return root

    return left_common_node if left_common_node is not None else right_common_node

def get_parent_node(root, node):
    """returns the parent node of the given node"""

    if not root:
        return None
    if(root.left and root.left.key == node):
        return root
    if (root.right and root.right.key == node):
        return root
    return (get_parent_node(root.left,node) or get_parent_node(root.right,node))

if __name__ == "__main__":
    #Create a binary tree
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.right.right = Node(6)
    firstNearestCommonParent = get_nearest_common_parent(root, 4, 6)
    secondNearestCommonParent = get_parent_node(root, firstNearestCommonParent.key)
    print("The nearest common parent for %d and %d is " % (4, 6))
    if secondNearestCommonParent is not None:
        print(firstNearestCommonParent.key, secondNearestCommonParent.key)
    else:
        print(firstNearestCommonParent.key)




