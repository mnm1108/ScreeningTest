import unittest
import unittest.mock
import io
import nearestcommonparent as ncp

class TestCommonParent(unittest.TestCase):

    def test_1(self):
        root = ncp.Node(2)
        root.left = ncp.Node(4)
        root.right = ncp.Node(6)
        root.left.left = ncp.Node(8)
        root.left.right = ncp.Node(10)
        root.left.left.left = ncp.Node(12)
        self.assertEqual(ncp.get_nearest_common_parent(root, 12, 10).key, 4)
        self.assertEqual(ncp.get_parent_node(root, ncp.get_nearest_common_parent(root, 12, 10).key).key, 2)
        self.assertEqual(ncp.get_nearest_common_parent(root, 6, 8).key, 2)

if __name__ == "__main__":
    unittest.main()
